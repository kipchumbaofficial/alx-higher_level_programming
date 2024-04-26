#!/usr/bin/python3
'''Takes in URL and Email
    Sends a POST to URL with email as parameter
'''


if __name__ == "__main__":
    import sys
    from urllib import request, parse

    url = sys.argv[1]

    query = {'email': sys.argv[2]}

    data = parse.urlencode(query).encode('ascii')
    req = request.Request(url, data)

    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
