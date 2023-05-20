from django.shortcuts import render,redirect
from . import models
import math
from datetime import datetime
from django.contrib.admin.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import datetime
from hashlib import sha512, sha256
from .merkleTree import merkleTree
from .xtra import *
from django.urls import reverse
from pytz import timezone
from django.contrib.auth.decorators import login_required



def home(request):
    error = False
    try:
        time = get_vote_auth()
        format = "%d/%m/%Y at %H:%M:%S %Z%z"
        asia_start = time[0].start.astimezone(timezone("Asia/Kolkata"))
        asia_end = time[0].end.astimezone(timezone('Asia/Kolkata'))
        context = {
            'error' : error,
            'start' : asia_start.strftime(format),
            'end' : asia_end.strftime(format),
        }
    except:
        error = True
        context = {
            'error' : error
        }

    return render(request, 'poll/home.html',context)

def otp(request):
    if request.method == "POST":
        otp =request.POST.get('otp')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        Voter = models.VoterList.objects.filter(username=username)[0]
        fail = ''
        if int(otp) == int(Voter.otp):
            if password == password1:
                if not models.Voter.objects.filter(username=username).exists():
                    d,n,e = keyGen()
                    phrase = passPhrase()
                    user = User.objects.create_user(username=username,password=password)

                    voter = models.Voter(username=username)
                    voter.public_key_n = n
                    voter.public_key_e = e
                    voter.has_voted = False

                    voterpvt = models.VoterPvt(username=username)
                    voterpvt.private_key_d,voterpvt.private_key_n,voterpvt.salt = encrypt(phrase,str(d),str(n))

                    sms(Voter.ph_country_code+Voter.phone_number," DO NOT SHARE THIS PASSPHRASE WITH ANYONE! \n\nYour Secret Passphrase is " + phrase)

                    user.save()
                    voter.save()
                    voterpvt.save()
                    context = {
                        'code' : phrase,
                    }

                    return render(request,'poll/success.html/',context)
                else:
                    fail = 'Voter Already Exists'
            else:
                fail = 'Password MisMatch!'
        else:
            fail = 'OTP is Invalid'
        return render(request,'poll/failure.html/',{'fail':fail})
    return redirect('home')


def register(request):
    time = get_vote_auth()
    format = "%d/%m/%Y at %H:%M:%S %Z%z"
    if time[0].end<datetime.datetime.now(datetime.timezone.utc):
        asia = time[0].end.astimezone(timezone('Asia/Kolkata'))
        context = {
            'fail' : "Cannot Register! Voting ended on "+asia.strftime(format),
        }
        return render(request,'poll/failure.html',context)
    if request.method=='POST':
        username = request.POST.get('username')
        validVoter = models.VoterList.objects.filter(username=username).exists()
        Registered = models.Voter.objects.filter(username=username).exists()
        if validVoter:
            if not Registered:
                voter = models.VoterList.objects.filter(username=username)[0]
                otp_number = otp_gen()
                voter.otp = otp_number
                voter.save()
                sms(voter.ph_country_code+voter.phone_number,"Your OTP is " + str(otp_number))
                context = {
                    'username' : username,
                    'country_code' : voter.ph_country_code,
                    'starred' : "*******"+str(voter.phone_number)[-3:]
                }
                return render(request,'registration/otp.html/',context)
            return render(request,'poll/failure.html',{'fail' : 'Voter is Already Registered!'})
        

        else:
            return render(request,'poll/failure.html',{'fail' : 'Invalid Voter!'})
    return render(request,'registration/register.html/')

@login_required(login_url='login')
def vote(request):
    candidates = models.Candidate.objects.all()
    context = {'candidates': candidates}
    return render(request, 'poll/vote.html', context)

def signin(request):
    time = get_vote_auth()
    if time[0].end>datetime.datetime.now(datetime.timezone.utc) and time[0].start<datetime.datetime.now(datetime.timezone.utc):    
        if request.method == 'POST':
            form = AuthenticationForm(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return redirect(reverse('vote'))
            else:
                return render(request,'poll/failure.html',{'fail':'Invalid Credentials! Try Logging In Again.'})  
        else:
            form = AuthenticationForm()
        return render(request,'registration/login.html',{'form':form})
    else:
        format = "%d/%m/%Y at %H:%M:%S %Z%z"
        if time[0].end<datetime.datetime.now(datetime.timezone.utc):
            asia = time[0].end.astimezone(timezone('Asia/Kolkata'))
            context = {
                'fail' : "Voting ended on "+asia.strftime(format),
            }
        elif time[0].start>datetime.datetime.now(datetime.timezone.utc):
            asia = time[0].start.astimezone(timezone("Asia/Kolkata"))
            context = {
                'fail' : "Voting will start on "+asia.strftime(format),
            }
        return render(request,'poll/failure.html',context)

@login_required(login_url='login')
def create(request, pk):
    voter = models.Voter.objects.filter(username=request.user.username)[0]
    if request.method == 'POST' and request.user.is_authenticated and not voter.has_voted:
        vote = pk
        lenVoteList = len(models.Vote.objects.all())
        if (lenVoteList > 0):
            block_id = math.floor(lenVoteList / 5) + 1
        else:
            block_id = 1

        phrase = request.POST.get('phrase')
        username = request.user.username
        
        voterpvt = models.VoterPvt.objects.filter(username=username).values()

        try:
            privateKey_d,privateKey_n=decrypt(phrase,voterpvt[0]['private_key_d'],voterpvt[0]['private_key_n'],voterpvt[0]['salt'])
        except:
            logout(request)
            return render(request,'poll/failure.html',{'fail':'Invalid Passphrase Please Login And Vote Again.'})   

        priv_key = {'n': int(privateKey_n), 'd':int(privateKey_d)}
        pub_key = {'n':int(voter.public_key_n), 'e':int(voter.public_key_e)}
        timestamp = datetime.datetime.now().timestamp()
        ballot = "{}|{}".format(vote, timestamp)
        h = int.from_bytes(sha512(ballot.encode()).digest(), byteorder='big')
        signature = pow(h, priv_key['d'], priv_key['n'])

        hfromSignature = pow(signature, pub_key['e'], pub_key['n'])

        if(hfromSignature == h):
            new_vote = models.Vote(vote=pk)
            new_vote.block_id = block_id
            voter.has_voted = True
            voter.save()
            new_vote.save()
            status = 'Ballot signed successfully'

        context = {
            'ballot': ballot,
            'signature': signature,
            'status': status,
            'id' : new_vote.id
        }
        return render(request, 'poll/status.html', context)
    logout(request)
    return render(request, 'poll/failure.html',{'fail':'It appears you have already voted!'})


@login_required(login_url='login')
def seal(request):

    if request.method == 'POST':
        vote_id = request.POST.get('vote_id')
        if (len(models.Vote.objects.all()) % 5 != 0):
            logout(request)
            return render(request,'poll/votesuccess.html',{'code' : vote_id})
        else:
            transactions = models.Vote.objects.order_by('block_id').reverse()
            transactions = list(transactions)[:5]
            block_id = transactions[0].block_id

            str_transactions = [str(x) for x in transactions]

            merkle_tree = merkleTree.merkleTree()
            merkle_tree.makeTreeFromArray(str_transactions)
            merkle_hash = merkle_tree.calculateMerkleRoot()

            nonce = 0
            timestamp = datetime.datetime.now().timestamp()

            vote_auth = models.VoteAuth.objects.get(username='admin')
            prev_hash = vote_auth.prev_hash
            while True:
                self_hash = sha256('{}{}{}{}'.format(prev_hash, merkle_hash, nonce, timestamp).encode()).hexdigest()
                if self_hash[0] == '0':
                    break
                nonce += 1
            vote_auth.prev_hash = self_hash
            vote_auth.save()
            block = models.Block(id=block_id,prev_hash=prev_hash,self_hash=self_hash,merkle_hash=merkle_hash,nonce=nonce,timestamp=timestamp)
            block.save()
            print('Block {} has been mined'.format(block_id))
            logout(request)
            return render(request,'poll/votesuccess.html',{'code' : vote_id})
    logout(request)
    return redirect("home")

def retDate(v):
    v.timestamp = datetime.datetime.fromtimestamp(v.timestamp)
    return v

def verify(request):
    time = get_vote_auth()
    if time[0].end<datetime.datetime.now(datetime.timezone.utc):
        if request.method == 'GET':
            verification = ''
            tampered_block_list = verifyVotes()
            votes = []
            if tampered_block_list:
                verification = 'Verification Failed. Following blocks have been tampered --> {}.\
                    The authority will resolve the issue'.format(tampered_block_list)
                error = True
            else:
                verification = 'Verification successful. All votes are intact!'
                error = False
                votes = models.Vote.objects.order_by('timestamp')
                votes = [retDate(x) for x in votes]
                
            context = {'verification':verification, 'error':error, 'votes':votes}
            return render(request, 'poll/verification.html', context)
        if request.method == 'POST':
            unique_id = request.POST.get('unique_id')
            try:
                tampered_block_list = verifyVotes()
                if tampered_block_list:
                    verification = 'Verification Failed. Following blocks have been tampered --> {}.\
                    The authority will resolve the issue'.format(tampered_block_list)
                    error = True
                else:
                    verification = 'Verification successful. The Vote is intact!'
                    error = False
                    vote = models.Vote.objects.filter(id=unique_id)
                    vote = [retDate(x) for x in vote]
            except:
                vote = []
                error = True
                verification = 'Invalid Unique ID'
            context = {'verification':verification, 'error':error, 'votes':vote}
            return render(request, 'poll/verification.html', context)
    else:
        format = "%d/%m/%Y at %H:%M:%S %Z%z"
        asia = time[0].end.astimezone(timezone('Asia/Kolkata'))
        context = {
            'fail' : "Verification will enable on "+asia.strftime(format),
        }
        return render(request,'poll/failure.html',context)



def result(request):
    time = get_vote_auth()
    if time[0].end<datetime.datetime.now(datetime.timezone.utc):
        if request.method == "GET":
            voteVerification = verifyVotes()
            if len(voteVerification):
                    return render(request, 'poll/verification.html', {'verification':"Verification failed.\
                    Votes have been tampered in following blocks --> {}. The authority \
                        will resolve the issue".format(voteVerification), 'error':True})

            vote_auth = models.VoteAuth.objects.get(username='admin')
            resultCalculated = vote_auth.resultCalculated
            if not resultCalculated:
                vote_auth.resultCalculated = True
                vote_auth.save() 
                list_of_votes = models.Vote.objects.all()
                for vote in list_of_votes:
                    candidate = models.Candidate.objects.filter(candidateID=vote.vote)[0]
                    candidate.count += 1
                    candidate.save()
                    
            context = {"candidates":models.Candidate.objects.order_by('count'), "winner":models.Candidate.objects.order_by('count').reverse()[0]}
            return render(request, 'poll/results.html', context)
    else:
        format = "%d/%m/%Y at %H:%M:%S %Z%z"
        asia = time[0].end.astimezone(timezone('Asia/Kolkata'))
        context = {
            'fail' : "Result will be displayed after "+asia.strftime(format),
        }
        return render(request,'poll/failure.html',context)


def verifyVotes():
    block_count = models.Block.objects.count()
    tampered_block_list = []
    for i in range (1, block_count+1):
        block = models.Block.objects.get(id=i)
        transactions = models.Vote.objects.filter(block_id=i)
        str_transactions = [str(x) for x in transactions]

        merkle_tree = merkleTree.merkleTree()
        merkle_tree.makeTreeFromArray(str_transactions)
        merkle_tree.calculateMerkleRoot()

        if (block.merkle_hash == merkle_tree.getMerkleRoot()):
            continue
        else:
            tampered_block_list.append(i)

    return tampered_block_list