#!/bin/bash
# Tested: 2025-05-07
# Tested by: Becky
# Tested on: GCP, Ubuntu 20.04 LTS
# Result:

cd /sparta-test-app-repo/app
echo ------ Running npm install... ------
npm install
echo

echo ------ Changing Adding DB_HOST variable... ------
export DB_HOST=mongodb://10.200.0.27:27017/posts
echo

echo ------ Starting Sparta App in background with pm2... ------
pm2 start app.js
echo