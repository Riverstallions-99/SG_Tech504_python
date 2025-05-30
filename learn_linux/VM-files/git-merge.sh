#!/bin/bash

# Checkout main
git fetch origin
git checkout main
git pull origin main

# Merge develop
git merge origin/develop -m "Automated merge from develop to main"

# Push changes
git push origin main