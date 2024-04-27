#!/usr/bin/python3
"""Takes in Github Credentilas
Uses github API to display your id
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    username = argv[1]
    token = argv[2]
    url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(username, token)

    response = requests.post(url, auth=auth)
    json_response = response.json()

    if json_response:
        identity = json_response.get('id')
        print(identity)
