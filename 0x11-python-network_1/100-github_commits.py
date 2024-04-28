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

    for i in range(10, 0, -1):
        sha = json_response[i].get('sha')
        commit = json_response[i].get('commit')
        author = commit.get('author')
        name = author.get('name')
        print(f"{sha} {name}")
