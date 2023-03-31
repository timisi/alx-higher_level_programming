#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""


import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {}
    values['email'] = sys.argv[2]
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page_info = response.read().decode('utf-8')
        print(page_info)
