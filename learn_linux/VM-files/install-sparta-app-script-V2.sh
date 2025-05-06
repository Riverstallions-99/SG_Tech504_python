#!/bin/bash
# Tested: 2025-05-06
# Tested by: Becky
# Tested on: GCP, Ubuntu 20.04 LTS
# Result: NO LONGER IN USE

echo Getting updates...
apt-get update 2>> ./install-errors.txt
echo Done.
echo
echo Upgrading packages...
sudo apt-get upgrade -y 2>> ./install-errors.txt
echo Done.
echo

echo Installing nginx package...
sudo apt-get install nginx -y 2>> ./install-errors.txt
echo Done.
echo

echo Installing pm2...
sudo npm install pm2 -y 2>> ./install-errors.txt
echo Done.
echo

echo Installing unzip package...
sudo apt-get install unzip 2>> ./install-errors.txt
echo Done.
echo

echo Downloading Sparta Test App from git repo...
git clone https://github.com/Riverstallions-99/sparta-test-app-repo 2>> ./install-errors.txt
echo Done.
echo

cd sparta-test-app-repo

echo Unzipping file...
unzip nodejs20-sparta-test-app.zip 2>> ../install-errors.txt
echo Done.
echo

echo Downloading NodeJS 20
sudo bash -c "curl -fsSL https://deb.nodesource.com/setup_20.x | bash -" 2>> ../install-errors.txt
echo Done.
echo
echo Installing NodeJS 20
sudo apt-get install nodejs -y 2>> ../install-errors.txt
echo Done.
echo

cd app

echo "Installing npm (NodeJS Package Manager)..."
npm install 2>> ../../install-errors.txt
echo Done.
echo

echo Stopping any rogue processes...
sudo kill $(ps aux | grep 'nginx' | awk '{print $2}')
sudo kill $(ps aux | grep 'npm' | awk '{print $2}')
sudo kill $(ps aux | grep 'node*' | awk '{print $2}')
echo Done.
echo

echo Stopping any running pm2 apps...
pm2 stop all
echo Done
echo

echo Starting Sparta App in background with pm2...
pm2 start & 2>> ../../install-errors.txt
echo Done.

exit 0
