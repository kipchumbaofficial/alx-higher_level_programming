#!/usr/bin/python3
"""Takes in Github Credentilas
Uses github API to display your id
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    auth = HTTPBasicAuth(argv[1], argv[2])

    response = requests.post('https://api.github.com/user', auth=auth)
    if response.status_code == 200:
        json_response = response.json()

        if json_response:
             print(json_response.get('id'))
    else:
        print("None")
