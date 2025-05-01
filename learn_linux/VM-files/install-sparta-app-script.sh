#!/bin/bash

echo Getting updates...
sudo apt-get update 2>> ./install-errors.txt
echo Retrieved updates successfully
echo

echo Upgrading packages...
sudo apt-get upgrade -y 2>> ./install-errors.txt
echo Packages upgraded successfully
echo

echo Installing nginx package...
sudo apt-get install nginx -y 2>> ./install-errors.txt
echo nginx installed successfully
echo

echo Installing unzip package...
sudo apt-get install unzip 2>> ./install-errors.txt
echo unzip installed successfully
echo

cd .hiddenZip
cp nodejs20-sparta-test-app.zip ../
cd ..

echo Unzipping file...
unzip nodejs20-sparta-test-app.zip 2>> ./install-errors.txt
echo Unzipped file successfully
echo

echo Downloading NodeJS 20
sudo bash -c "curl -fsSL https://deb.nodesource.com/setup_20.x | bash -" 2>>>
echo Downloaded NodeJS Version 20 successfully
echo Installing NodeJS 20
sudo apt-get install nodejs -y 2>> ./install-errors.txt
echo Installed NodeJS Version 20 successfully
echo

cd app

echo Installing npm (NodeJS Package Manager)...
sudo npm install 2>> ./install-errors.txt
echo Installed npm successfully
echo

echo Starting npm...
npm start 2>> ./install-errors.txt
