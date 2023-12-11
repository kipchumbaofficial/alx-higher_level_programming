#!/bin/bash

# Stage Changes for commit
git add .

# Get the commit Message
echo "Enter the commit message"
read commitMessage

# Commit changes
git commit -m "$commitMessage"

# Push Changes
git push
