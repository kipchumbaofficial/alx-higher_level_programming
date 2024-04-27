#!/usr/bin/python3
"""Takes in a letter
sends a POST requests with letter as parameter
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    payload = {'q': ""}
    if len(argv) > 1:
        payload['q'] = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=payload)

    if 'application/json' in response.headers.get('Content-Type', ''):
        json_response = response.json()
        if not json_response:
            print("No result")
        else:
            identity = json_response.get('id')
            name = json_response.get('name')
            print(f"{[identity]} {name}")
    else:
        print("Not a valid JSON")
