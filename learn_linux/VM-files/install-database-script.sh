#!/bin/bash
# Tested: 2025-05-01
# Tested by: Becky
# Tested on: GCP, Ubuntu 22.04 LTS
# Result: Ran successfully on fresh VM and as a start up script for a fresh VM

echo Updating...
sudo apt-get update
echo Done.
echo

echo Upgrading...
sudo DEBIAN_FRONTEND="noninteractive" apt-get upgrade -y
echo Done.
echo

echo Installing gnupg and curl...
sudo apt-get install gnupg curl 2>> provision-error-logs.txt
echo Done.
echo

echo Importing MongoDB public GPG key...
# sudo rm -f /usr/share/keyrings/mongodb-server-7.0.gpg
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor --yes
echo Done.
echo

echo Creating list file for Ubuntu 22.04...
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
echo Done.
echo

echo Reloading the package database
sudo apt-get update
echo Done.
echo

echo Installing MongoDB 7.0.6
# install mongodb 7.0.6 packages
sudo DEBIAN_FRONTEND="noninteractive" apt-get install -y \
   mongodb-org=7.0.6 \
   mongodb-org-database=7.0.6 \
   mongodb-org-server=7.0.6 \
   mongodb-mongosh \
   mongodb-org-shell=7.0.6 \
   mongodb-org-mongos=7.0.6 \
   mongodb-org-tools=7.0.6 \
   mongodb-org-database-tools-extra=7.0.6
echo Done.
echo

echo Changing MongoDB config...
# not enabled once installed, so make changes first, then start MongoDB
# configure mongodb - bind IP from 127.0.0.1 to 0.0.0.0
sudo sed -i 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/g' /etc/mongod.conf
echo Done.
echo

echo Starting MongoDB...
# start mongodb
sudo systemctl start mongod
echo Done.
echo

echo Enabling MongoDB...
# enable mongodb (systemctl enable mongodb)
sudo systemctl enable mongod
echo Done.
echo