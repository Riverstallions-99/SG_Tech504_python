#!/bin/bash

rm install-errors.txt

sudo kill $(ps aux | grep 'nginx' | awk '{print $2}')
sudo kill $(ps aux | grep 'npm' | awk '{print $2}')
sudo kill $(ps aux | grep 'node*' | awk '{print $2}')

sudo rm -r sparta-test-app-repo/
sudo apt remove unzip -y
sudo apt remove nginx -y
sudo apt remove nodejs -y

sudo rm -r ~/.npm

sudo apt-get autoremove -y
