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

# Self-hosting (For Devs)

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
# Start Server
$ python(3) manage.py runserver 0.0.0.0:80
# Head over to http://127.0.0.1/ to see the website.
```

# Mandatory Configs
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
<img width="960" alt="vote_verification" src="https://user-images.githubusercontent.com/54449305/80915076-5679dc80-8d6d-11ea-9650-3fe960bd9896.png">

<img width="960" alt="user-authentication" src="https://user-images.githubusercontent.com/54449305/80915092-73161480-8d6d-11ea-923a-15f4788d8e40.png">

![vote_page](https://user-images.githubusercontent.com/54449305/80915104-8a550200-8d6d-11ea-9880-d0c111d4d096.png)


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

