#!/usr/bin/python3
"""Takes in URL
    Sends a request and displays values of X-Request-Id
"""
if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers['X-Request-Id'])
