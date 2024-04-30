#!/usr/bin/python3
"""Takes in a repo and owner
prints out sha and author of commit
"""

if __name__ == "__main__":
    from sys import argv
    import requests
    url = f'https://api.github.com/repos/{argv[1]}/{argv[2]}/commits'
    response = requests.get(url)

    info = response.json()
    for i in range(10):
        print(info[i].get('sha'), end=": ")
        print(info[i].get('commit').get('author').get('name'))
