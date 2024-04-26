#!/usr/bin/python3
"""Fetches a URL using requests
"""


if __name__ == "__main__":
    import requests

    response = requests.get("https://alx-intranet.hbtn.io/status")
    resp = response.text
    print("Body response:")
    print(f"\t- type: {type(resp)}")
    print(f"\t- content: {resp}")
