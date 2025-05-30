#!/bin/bash

echo "SSH-ing into EC2 instance to run first script..."
ssh -o StrictHostKeyChecking=no ubuntu@172.31.45.25 << EOF
    echo "removing old app..."
    sudo rm -r /home/ubuntu/app/
EOF

# SCP packaged code to hardcoded EC2 instance IP address
echo "SCP-ing packaged app to EC2 instance"
scp -rvo StrictHostKeyChecking=no app/ ubuntu@172.31.45.25:/home/ubuntu/
echo "SSH-ing into EC2 instance to run script..."
ssh -o StrictHostKeyChecking=no ubuntu@172.31.45.25 << EOF
    echo "moving into app/..."
    cd /home/ubuntu/app/
    echo "installing packages with npm install..."
    npm install
    echo "stopping old pm2 instances..."
    pm2 stop all
    echo "starting app with pm2..."
	pm2 start app.js
EOF