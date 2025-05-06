#!/bin/bash
# Tested: 2025-05-06
# Tested by: Becky
# Tested on: GCP, Ubuntu 20.04 LTS
# Result: Runs successfully on fresh machine but not as script for VM creation...

cd ~

echo Getting updates...
apt-get update
echo Done.
echo
echo Upgrading packages...
sudo apt-get upgrade -y
echo Done.
echo

echo Installing nginx package...
sudo apt-get install nginx -y
echo Done.
echo

echo Installing unzip package...
sudo apt-get install unzip
echo Done.
echo

sudo rm -r sparta-test-app-repo
echo Downloading Sparta Test App from git repo...
git clone https://github.com/Riverstallions-99/sparta-test-app-repo
echo Done.
echo

cd sparta-test-app-repo

echo Unzipping file...
unzip nodejs20-sparta-test-app.zip
echo Done.
echo

echo Downloading NodeJS 20
sudo bash -c "curl -fsSL https://deb.nodesource.com/setup_20.x | bash -"
echo Done.
echo
echo Installing NodeJS 20
sudo apt-get install nodejs -y
echo Done.
echo

cd app

echo "Installing npm (NodeJS Package Manager)..."
npm install
echo Done.
echo

echo Installing pm2
sudo npm install pm2@latest -g
echo Done.
echo

echo Stopping any running pm2 apps...
pm2 stop all
echo Done
echo

echo Changing Adding DB_HOST variable...
export DB_HOST=mongodb://10.200.0.10:27017/posts
source ~/.bashrc
echo Done.
echo

echo Changing nginx config file...
sudo sed -i 's%try_files $uri $uri =404;%proxy_pass http://localhost:3000;%g' /etc/nginx/sites-available/default
sudo systemctl restart nginx
echo Done.
echo

echo Starting Sparta App in background with pm2...
pm2 start app.js
echo Done.

exit 0
