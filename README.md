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


# Mandatory Configs

1. Go to [API NINJA](https://api-ninjas.com/) and signup to obtain the api key for passphrase generation.
2. Create an Account on [TWILIO](https://www.twilio.com/try-twilio) and Buy a Phone Number to use the OTP Service.

Fill the env file with the obtained APIs.

```
[+] Create a env file in the root directory for the api tokens
    [-] DJANGO_SECRET_KEY=
    [-] DEBUG=
    [-] DJANGO_ALLOWED_HOSTS=
    [-] DJANGO_CSRF_TRUSTED_ORIGINS=
    [-] API_NINJA_API =
    [-] TWILIO_ACCOUNT_SID =
    [-] TWILIO_AUTH_TOKEN = 
    [-] TWILIO_PHONE_NUMBER = 
```
## An Example Of "env" File
```
DJANGO_SECRET_KEY=#sdfgg4g7h%-y8b+34_^s$yo^$a63&*$Fb3^d
DEBUG=False
DJANGO_ALLOWED_HOSTS=10.1.1.50
API_NINJA_API=/ghjf53spoG657vghjygdr0qw==uRVWERV
TWILIO_ACCOUNT_SID=AA3w5fgdrfawd3459faedw4349a3b
TWILIO_AUTH_TOKEN=awd18f3ccac7329thfsf43fd4drgx1
TWILIO_PHONE_NUMBER=+134656544
DJANGO_CSRF_TRUSTED_ORIGINS=https://10.1.1.50
```

# Z-vote Deployment On [Raspberrypi Docker Container](https://github.com/akkupy/Homelab)

## Install Docker and Portainer if not already done.([refer here](https://github.com/akkupy/Homelab#installation-of-docker-and-portainer))


### Folder Setup Script

1. First thing we need to do is setup the folder structure. 

Run the following script
```
wget -qO- https://raw.githubusercontent.com/akkupy/Homelab/main/scripts/zvote_dir.sh | sudo bash
```

2. Now we need to move into that directory using the following:

```
cd /home/$USER/zvote
```
3. Create an 'env' file 

```
sudo nano env
```

4. Fill the environment variables([see above](https://github.com/akkupy/Z-Vote/tree/production#mandatory-configs))

5. Pull the docker image of [z-vote](https://hub.docker.com/r/akkupy/z-vote)

```
docker pull akkupy/z-vote:latest
```
6. Run the container

```
docker run -d \
  --name=z-vote \
  -e PUID=1000 \
  -e PGID=1000 \
  --env-file env \
  -p 8100:8100 \
  -v ./static:/app/static \
  --restart unless-stopped \
  akkupy/z-vote:latest
```

7. Exec into the container using the command below

```
docker exec -it z-vote sh
```
* You will see a new terminal like shown below.

```
/app #
```

8. Run the following commands on the container terminal.

* Enter the username and password for the superuser when prompted.

```
python manage.py makemigrations poll
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```
9. Press Ctrl+D to exit the container Terminal.

## Install Nginx Proxy Manager if not already done([refer here](https://github.com/akkupy/Homelab/blob/main/docs/nginx_proxy_manager.md)).

### Add a new volume(given below) to the nginx proxy manager container using portainer.

```
/home/$USER/zvote/static:/data/static
```

### Setting up Nginx Proxy Manager for Z-vote
<br>

Go to login screen.
![First Login](https://raw.githubusercontent.com/akkupy/Homelab/main/images/nginx-proxy-manager-First-Login.png)

### Select Hosts > Proxy Hosts

![Proxy Hosts](https://raw.githubusercontent.com/akkupy/Homelab/main/images/nginx-proxy-manager-Proxy-Host.png)

Select Add Proxy Hosts

![Proxy Hosts](https://raw.githubusercontent.com/akkupy/Homelab/main/images/nginx-proxy-manager-Menu-Add-Proxy-Host.png)

We need to enter the proxy information.  In this example we are going to use the following information.

Secure External connections to the service using https.<br>
Domain Name: homer.example.com<br>
Scheme: https<br>
Forward Hostname/IP address: 192.168.1.23<br>
Port: 8902<br>
Cache Assets: Disabled<br>
Block Common Exploits: Enabled<br>
Websockets Support: Disabled<br>
Accesss List: Publicly Accessible<br>

> Most of these options should be self explanatory if you aren't sure what they do it is likely best to leave them disabled.

The most import options.<br>  
Domain Name is the public Domain name that will point at your host.<br>
Forward Hostname/IP is the server running the resource.<br>
Port is the port the service is running on that server.<br>


![Proxy Hosts](https://raw.githubusercontent.com/akkupy/Homelab/main/images/nginx-proxy-manager-New-Proxy-Host.png)

> Hint: Generating Certificates can be complicated I will be outlining one of the simplest ways to generate one.  There are other ways not outlined here.

Now we need to setup our secure https connection to the server.  Select the SSL tab.

## Method 1(Recommended for internet based usage):

Under SSL Certificates we are going to select Request a new SSL Certificate.

I am also going to select Force SSL this will prevent non-secure connections from being used.  

I will agree to the terms after reading them you should at least review them once so you understand the terms of service.

It should have your correct email address listed if it doesn't please fix as this is where you will get alerts if there is an issue with the Certificate.

![Proxy Hosts](https://raw.githubusercontent.com/akkupy/Homelab/main/images/nginx-proxy-manager-New-Proxy-Host-SSL.png)

Once you click Save it will generate a new certificate this can take a few minutes to do.

## Method 2(Recommended for Local usage and usage with [tailscale](https://github.com/akkupy/Homelab/blob/main/docs/tailscale.md)):

You can use a self generated SSL certificate(which can be generated [here](https://github.com/akkupy/Self_Signed_SSL_Cerificate)).In this case select Custom under the SSL Certificates and upload the key and certificate generated.

## Post SSL Certificate Gerneration Go to Advanced Tab

* Paste the Nginx Configuration given below(Change proxy_pass address to the one defined on details page).

```
location /static/{
                 root /data;
        }
    location / {
          proxy_pass http://<ip>:<port>;
    }

```


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
## * Create env file([refer here](https://github.com/akkupy/Z-Vote/tree/production#mandatory-configs))

## * Run and Configure the container([refer here](https://github.com/akkupy/Z-Vote/tree/production#z-vote-deployment-on-raspberrypi-docker-container))



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

