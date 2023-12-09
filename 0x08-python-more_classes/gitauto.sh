#!/bin/bash

# Stage changes
git add .

# Read the commit message
echo "Enter the commit message"
read commitMessage

# Commit the changes
git commit -m "$commitMessage"

# Push changes to github
git push
