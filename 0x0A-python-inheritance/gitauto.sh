#!/bin/bash

# Stage changes for commit
git add .

# Read Commit message
echo "Enter the commit message"
read commitMessage

# Commit changes
git  commit -m "$commitMessage"

# Push to github
git push
