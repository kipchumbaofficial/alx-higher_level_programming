#!/usr/bin/python3
"""Takes in a repo and owner
prints out sha and author of commit
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    response = requests.get(url)
    info = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                info[i].get("sha"),
                info[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
