#!/bin/bash
# Tested: 2025-05-07
# Tested by: Becky
# Tested on: GCP, Ubuntu 20.04 LTS
# Result: Runs successfully on fresh machine and as script for VM creation

echo ------ Getting updates... ------
apt-get update
echo ------ Done. ------
echo
echo ------ Upgrading packages... ------
sudo DEBIAN_FRONTEND="noninteractive" apt-get upgrade -y
echo ------ Done. ------
echo

echo ------ Installing nginx package... ------
sudo DEBIAN_FRONTEND="noninteractive" apt-get install nginx -y
echo ------ Done. ------
echo

echo ------ Installing unzip package... ------
sudo DEBIAN_FRONTEND="noninteractive" apt-get install unzip
echo ------ Done. ------
echo

sudo rm -r sparta-test-app-repo
echo ------ Downloading Sparta Test App from git repo... ------
git clone https://github.com/Riverstallions-99/sparta-test-app-repo
echo ------ Done. ------
echo

cd sparta-test-app-repo

echo ------ Unzipping file... ------
unzip nodejs20-sparta-test-app.zip
echo ------ Done. ------
echo

echo ------ Downloading NodeJS 20...  ------
sudo bash -c "curl -fsSL https://deb.nodesource.com/setup_20.x | bash -"
echo ------ Done. ------
echo
echo ------ Installing NodeJS 20... ------
sudo DEBIAN_FRONTEND="noninteractive" apt-get install nodejs -y
echo ------ Done. ------
echo

cd app

echo "------ Installing npm (NodeJS Package Manager)... ------"
npm install
echo ------ Done. ------
echo

echo ------ Installing pm2... ------
sudo DEBIAN_FRONTEND="noninteractive" npm install pm2@latest -g
echo ------ Done. ------
echo

echo ------ Stopping any running pm2 apps... ------
pm2 stop all
echo ------ Done. ------
echo

echo ------ Changing Adding DB_HOST variable... ------
export DB_HOST=mongodb://172.31.36.130:27017/posts
echo ------ Done. ------
echo

echo ------ Changing nginx config file... ------
sudo sed -i 's%try_files $uri $uri/ =404;%proxy_pass http://localhost:3000;%g' /etc/nginx/sites-available/default
sudo systemctl restart nginx
echo ------ Done. ------
echo

echo ------ Starting Sparta App in background with pm2... ------
pm2 start app.js
echo ------ Done. ------

exit 0