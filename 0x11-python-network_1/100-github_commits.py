#!/usr/bin/python3
"""Takes in a repo and owner
prints out sha and author of commit
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    repo = argv[1]
    owner = argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)

    json_response = response.json()
    info = json_response[-10:]
    for commit in reversed(info):
        sha = commit.get('sha')
        commit = commit.get('commit')
        author = commit.get('author')
        name = author.get('name')
        print(f"{sha} {name}")
