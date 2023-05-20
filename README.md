<p align="center"><a href="https://akkupy.me"><img src="https://www.mdpi.com/sensors/sensors-21-05874/article_deploy/html/images/sensors-21-05874-g004-550.jpg" width="5000"></a></p> 

<h1 align="center"><b>BlockChain Based E-Voting System</b></h1>

* This project aims at implementing a voting system based on Blockchain technology. 
* It is a secure, transparent and decentralized way of voting.
* It converts ballots into transactions and securely mines blocks out of them.
* The advantage of a blockchain based voting system include the ability to vote from any place and prevent any tampering of votes.


# Technology stack used:
1. Python 3.11.x
2. Django Web Framework 4.2.1
3. Bootstrap 4
4. DB SQLite 3
5. HTML5

# Z-vote Production Server On Docker ([click image](https://github.com/akkupy/Z-Vote/tree/production))

<p align="center"><a href="https://github.com/akkupy/Z-Vote/tree/production"><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/69421964/238869562-becd50b0-006d-4ae8-a47b-b19cdb4c98e4.png" width="400"></a></p> 



# Self-hosting(Development Server)

## Simply clone the repository and run the server:
```sh
# Install Git First // (Else You Can Download And Upload to Your Local Server)
$ git clone https://github.com/akkupy/Z-Vote.git

# Open Git Cloned File
$ cd Z-Vote

# Config Virtual Env (Skip is already Done.)
$ virtualenv -p /usr/bin/python3 venv
$ . ./venv/bin/activate

# Install All Requirements.
$ pip(3) install -r requirements.txt

# Run makemigrations and migrate command.
$ python(3) manage.py makemigrations poll
$ python(3) manage.py migrate

# Create a Superuser.
$ python(3) manage.py createsuperuser

# Create a .env file(See Below for more details.)

# Start Server
$ python(3) manage.py runserver 0.0.0.0:80
# Head over to http://127.0.0.1/ to see the website.

# Head over to http://127.0.0.1/admin to add the voterlists in 'Voter lists' table and the candidates in the 'Candidates' table.

# Set the Voting Time in 'Vote auths' table(Create only one object and add the start and end time of voting).

# Now the project is ready for Voting!
```

# Environment Variables

1. Go to [API NINJA](https://api-ninjas.com/) and signup to obtain the api key for passphrase generation.
2. Create an Account on [TWILIO](https://www.twilio.com/try-twilio) and Buy a Phone Number to use the OTP Service.

Fill the .env file with the obtained values.

```
[+] Create a .env file in the root directory for the api tokens
    [-] API_NINJA_API = ''
    [-] TWILIO_ACCOUNT_SID = ''
    [-] TWILIO_AUTH_TOKEN = ''
    [-] TWILIO_PHONE_NUMBER = ''
```


## An Example Of ".env" File
```
API_NINJA_API = '/ghjf53spoG657vghjygdr0qw==uRVWERV'
TWILIO_ACCOUNT_SID = 'AA3w5fgdrfawd3459faedw4349a3b'
TWILIO_AUTH_TOKEN = 'awd18f3ccac7329thfsf43fd4drgx1'
TWILIO_PHONE_NUMBER = '+134656544'
```

## Screenshots:

<h4 align="center"><b>Home Page</b></h4>

![home](https://github.com/akkupy/Z-Vote/assets/69421964/0373134c-70e1-44a6-ba28-e416c7390993)

<h4 align="center"><b>Register Page</b></h4>

![register](https://github.com/akkupy/Z-Vote/assets/69421964/c7f60ed3-e898-4b30-beca-8dda273ea79b)

<h4 align="center"><b>OTP Page</b></h4>

![otp](https://github.com/akkupy/Z-Vote/assets/69421964/c7a081e9-15b6-4ebb-ab59-eb29564a0a94)

<h4 align="center"><b>Registration Successful</b></h4>

![reg_succ](https://github.com/akkupy/Z-Vote/assets/69421964/5b86ca86-b4ee-467c-b00b-e24765ccfa54)

<h4 align="center"><b>Login Page</b></h4>

![login](https://github.com/akkupy/Z-Vote/assets/69421964/f2fe7b72-5d14-4411-a48e-bc2509721d6b)

<h4 align="center"><b>Voting Page</b></h4>

![vote](https://github.com/akkupy/Z-Vote/assets/69421964/808ab136-a80a-46be-ae9a-70d6f4740dad)

<h4 align="center"><b>Vote Verification Page</b></h4>

![verification](https://github.com/akkupy/Z-Vote/assets/69421964/8c1675de-1dbf-48ce-9305-7eff49f928d9)

<h4 align="center"><b>Result</b></h4>

![result](https://github.com/akkupy/Z-Vote/assets/69421964/32006491-cd8f-40f7-9c5a-84a6be11ced4)


# Contact Me
 [![telegram](https://img.shields.io/badge/Akku-000000?style=for-the-badge&logo=telegram)](https://t.me/akkupy)


# License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

This is a Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 



#### --This is only a demonstration of the blockchain based voting system and it is entirely a prototype of the technology--

