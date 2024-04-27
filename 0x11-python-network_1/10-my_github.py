#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    # github_username = str(sys.argv[1])
    # password_pat = str(sys.argv[2])
    # Setting the GitHub API URL
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    # Sending a GET request to the GitHub API
    response = requests.get("https://api.github.com/user", auth=auth)
    if response.status_code == 200:
        info = response.json()
        print("{}".format(info.get("id")))
    else:
        print("None")
