#!/bin/bash
# Tested: 2025-05-01
# Tested by: Becky
# Tested on: GCP, Ubuntu 22.04 LTS
# Result:

echo Updating...
sudo apt-get update
echo

echo Upgrading
sudo apt-get upgrade -y
# USER INPUT NEEDED
echo

# install gnupg and curl
sudo apt-get install gnupg curl
# import the MongoDB public GPG key
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor

# update packages
sudo apt-get update

# create list file for U 22.04
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

# reload the package database
sudo apt-get update

# install mongodb 7.0.6 packages
sudo apt-get install -y \
   mongodb-org=7.0.6 \
   mongodb-org-database=7.0.6 \
   mongodb-org-server=7.0.6 \
   mongodb-mongosh \
   mongodb-org-shell=7.0.6 \
   mongodb-org-mongos=7.0.6 \
   mongodb-org-tools=7.0.6 \
   mongodb-org-database-tools-extra=7.0.6

# not enabled once installed, so make changes first, then start MongoDB
# configure mongodb - bind IP from 127.0.0.1 to 0.0.0.0
# FIX THIS TO REPLACE STRING WITH ANOTHER STRING
sudo sed -i 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/g' /etc/mongod.conf

# start mongodb
sudo systemctl start mongod

# enable mongodb (systemctl enable mongodb)
sudo systemctl enable mongod