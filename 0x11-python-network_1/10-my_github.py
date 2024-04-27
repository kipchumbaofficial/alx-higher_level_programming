#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
You must use Basic Authentication with a personal access token as
password to access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case, a personal
access token as password)
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    # github_username = str(sys.argv[1])
    # password_pat = str(sys.argv[2])
    # Setting the GitHub API URL
    # my_github_api_url = "https://api.github.com/user"
    # Set up Basic Authentication using my username and PAT
    # I commented my code because of TypeError:
    # Error: TypeError: Cannot mix str and non-str arguments
    # I had to rename all my variables for it to work
    #
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    # Sending a GET request to the GitHub API
    response = requests.get("https://api.github.com/user", auth=auth)
    if response.status_code == 200:
        # Converting my GitHub API Response to a JSON dict so that I
        # can extract the id from it
        info = response.json()
        # Now, to print my GitHub ID
        print("{}".format(info.get("id")))
    else:
        print("None")
