#!/usr/bin/python3
'''Takes in URL
and displays value of X-Request-Id
'''


if __name__ == '__main__':
    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers['X-Request-Id'])
