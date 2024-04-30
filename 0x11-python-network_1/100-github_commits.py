#!/usr/bin/python3
"""Takes in a repo and owner
prints out sha and author of commit
"""

if __name__ == "__main__":
    from sys import argv
    import requests
    url = f'https://api.github.com/repos/{argv[1]}/{argv[2]}/commits'
    response = requests.get(url)

    info = response.json()[:10]
    for commit in reversed(info):
        name = commit.get('commit').get('author').get('name')
        print(f"{commit.get('sha')}: {name}")
