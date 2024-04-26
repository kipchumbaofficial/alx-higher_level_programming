#!/usr/bin/python3
'''Takes in a URL
    Displays body and Handles errors
'''


if __name__ == "__main__":
    from urllib import request
    from sys import argv
    import urllib.error

    try:
        url = argv[1]

        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
