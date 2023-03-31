#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""


import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        page_info = response.info()
        print(page_info.get('X-Request-Id'))
