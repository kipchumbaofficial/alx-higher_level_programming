#!/usr/bin/env bash


# Stage changes
git add .

# Read commit message
echo "Enter the commit message"
read commitMessage

# Commit message
git commit -m "$commitMessage"

# Push Changes to git hub
git push
