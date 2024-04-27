#!/usr/bin/python3
"""Takes in a repo and owner
prints out sha and author of commit
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    repo = argv[1]
    owner = argv[2]
    repo_parts = repo.split('/')
    rep, dire = repo_parts
    url = f'https://api.github.com/repos/{owner}/{rep}/commits?path={dire}'
    response = requests.get(url)

    json_response = response.json()
    for commits in json_response:
        sha = commits.get('sha')
        commit = commits.get('commit')
        author = commit.get('author')
        name = author.get('name')
        print(f"{sha} {name}")
