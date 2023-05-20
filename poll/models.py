from django.db import models
from uuid import uuid4
from datetime import datetime

# Create your models here.

def get_time():
    return datetime.now().timestamp()

class Candidate(models.Model):
    candidateID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    party = models.CharField(max_length=100)
    criminalRecords = models.BooleanField(default=False)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class VoterList(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    ph_country_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    otp = models.IntegerField(default=0)

    def __str__(self):
        return self.username
    
class Voter(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    public_key_n = models.CharField(max_length=320)
    public_key_e = models.IntegerField(default=0)
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class VoterPvt(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    salt = models.CharField(max_length=100)
    private_key_n = models.CharField(max_length=320)
    private_key_d = models.CharField(max_length=320)

    def __str__(self):
        return self.username

class Vote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    vote = models.IntegerField(default=0)
    timestamp = models.FloatField(default=get_time)
    block_id = models.IntegerField(null=True)

    def __str__(self):
        return "{}|{}|{}".format(self.id, self.vote, self.timestamp)

class Block(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    prev_hash = models.CharField(max_length=64, blank=True)
    merkle_hash = models.CharField(max_length=64, blank=True)
    self_hash = models.CharField(max_length=64, blank=True)
    nonce = models.IntegerField(null=True)
    timestamp = models.FloatField(default=get_time)

    def __str__(self):
        return str(self.self_hash)

class VoteAuth(models.Model):
    username = models.CharField(max_length=30,primary_key=True,default='admin')
    start = models.DateTimeField()
    end = models.DateTimeField()
    resultCalculated = models.BooleanField(default=False)
    prev_hash = models.CharField(max_length=100, default='0' * 64)