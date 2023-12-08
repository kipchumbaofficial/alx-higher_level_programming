#!/bin/bash

# Stage all the changes
git add .

# Read commit message
echo "Enter the commit message"
read commitMessage

git commit -m "$commitMessage"

git push
