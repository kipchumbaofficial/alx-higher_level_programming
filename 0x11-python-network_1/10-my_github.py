#!/usr/bin/python3
"""Takes in Github Credentilas
Uses github API to display your id
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    username = argv[1]
    token = argv[2]
    url = 'https://api.github.com/user'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(url, headers=headers, auth=(username, token))
    json_response = response.json()

    if json_response:
        identity = json_response.get('id')
        print(identity)
