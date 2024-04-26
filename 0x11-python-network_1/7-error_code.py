#!/usr/bin/python3
"""Handling Errors with requests"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
    elif response.status_code >= 400:
        print(f"Error code: {response.status_code}")
