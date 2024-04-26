#!/usr/bin/python3
'''POST with requests
'''


if __name__ == "__main__":
    import sys
    import requests

    load = {'email': sys.argv[2]}
    url = sys.argv[1]

    response = requests.post(url, data=load)
    print(response.text)
