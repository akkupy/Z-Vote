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


# Environment Variables.

1. Go to [API NINJA](https://api-ninjas.com/) and signup to obtain the api key for passphrase generation.
2. Create an Account on [TWILIO](https://www.twilio.com/try-twilio) and Buy a Phone Number to use the OTP Service.

Fill the env file with the obtained APIs.

```
[+] Create a env file in the root directory
    [-] DJANGO_SECRET_KEY=
    [-] DEBUG=
    [-] DJANGO_ALLOWED_HOSTS=
    [-] DJANGO_CSRF_TRUSTED_ORIGINS=
    [-] API_NINJA_API =
    [-] TWILIO_ACCOUNT_SID =
    [-] TWILIO_AUTH_TOKEN = 
    [-] TWILIO_PHONE_NUMBER = 
```
<br>

* <b>DJANGO_SECRET_KEY</b> - Enter the Django Project Secret Key.(Generate random key [here](https://djecrety.ir/)) .

* <b>DEBUG</b> - Debug state of Django Project(Set to empty for False).
  * ALWAYS set to FALSE during PRODUCTION.

  <br>

* <b>DJANGO_ALLOWED_HOSTS</b> - Enter the domain name or ip used for accessing the application.

* <b>DJANGO_CSRF_TRUSTED_ORIGINS</b> = Enter the link of your domain eg: https://domain_name.com or https://ip_address .

* <b>API_NINJA_API</b> - Enter the API Token of Api Ninja for generating random passphrase.

* <b>TWILIO_ACCOUNT_SID</b> - Enter the Twilio Account SID Obtained.

* <b>TWILIO_AUTH_TOKEN</b> - Enter the Twilio Auth Token Obtained.

* <b>TWILIO_PHONE_NUMBER</b> - Enter your Twilio Phone Number , Used for sending OTP.

<br>

## An Example Of "env" File
```
DJANGO_SECRET_KEY=#sdfgg4g7h%-y8b+34_^s$yo^$a63&*$Fb3^d
DEBUG=False
DJANGO_ALLOWED_HOSTS=vote.com
DJANGO_CSRF_TRUSTED_ORIGINS=https://vote.com
API_NINJA_API=/ghjf53spoG657vghjygdr0qw==uRVWERV
TWILIO_ACCOUNT_SID=AA3w5fgdrfawd3459faedw4349a3b
TWILIO_AUTH_TOKEN=awd18f3ccac7329thfsf43fd4drgx1
TWILIO_PHONE_NUMBER=+134656544
```
<br>

# Z-vote Production Deployment On Docker
<br>

## Install Docker and Portainer if not already done.([refer here](https://github.com/akkupy/Homelab#installation-of-docker-and-portainer))

<br>

### 1. Run the following script to clone the repository.
<br>

```
wget -qO- https://raw.githubusercontent.com/akkupy/Z-Vote/production/script/zvote.sh | bash
```
<br><br>
2. Now we need to move into that directory using the following:

```
cd /home/$USER/Z-Vote
```
<br><br>
3. Create an 'env' file .

```
sudo nano env
```
<br><br>

4. Fill the environment variables([see above](https://github.com/akkupy/Z-Vote/tree/production#environment-variables)).

<br><br>

5. Pull the docker image of [Z-Vote](https://hub.docker.com/r/akkupy/z-vote) and [Nginx](https://hub.docker.com/_/nginx).

```
docker pull akkupy/z-vote:latest
docker pull nginx:latest
```
<br><br>

## Change the ports of Nginx if you are already running a service on port 80 and 443 in the docker-compose.yml file

<br><br>


11. Generate a SSL Certificate and copy the .key and .crt files into the directory given below.

<br>

```
 cd /home/$USER/Z-Vote/nginx
```

<br>

* Rename the .key as vote.key and .crt as vote.crt
* A self generated SSL certificate(which can be generated [here](https://github.com/akkupy/Self_Signed_SSL_Cerificate))
* Use Self Generated SSL Certificate For Local and Private VPN Networks.

<br>


12. CD into the Z-Vote directory.

```
cd /home/$USER/Z-Vote
```
<br><br>

13. Run the following command to start the containers.

```
docker compose up -d
```
<br><br>

14. Exec into the container using the command below

```
docker exec -it zvote sh
```
<br><br>
* You will see a new terminal like shown below.

```
/app #
```
<br><br>
15. Run the following commands on the container terminal.

* Enter the username and password for the superuser when prompted.

```
python manage.py makemigrations poll
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```
<br><br>
16. Press Ctrl+D to exit the container Terminal.


<br><br>

### Head Over to your domain name to see the web application!




<br><br><br><br><br>


# Building Docker Container from Dockerfile (For Devs)

## * Clone the repository and Build the container:
```sh
# Install Git First // (Else You Can Download And Upload to Your Local Server)
$ git clone -b production https://github.com/akkupy/Z-Vote.git
# Open Git Cloned File
$ cd Z-Vote
# Run Docker Build
$ docker build -t <name>:<tag> .
```
## * Create env file([refer here](https://github.com/akkupy/Z-Vote/tree/production#environment-variables))

## * Run and Configure the container([refer here](https://github.com/akkupy/Z-Vote/tree/production#z-vote-production-deployment-on-docker))



<br><br><br>

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

