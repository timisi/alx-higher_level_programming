#!/usr/bin/python3
"""Python script that takes in a string and sends a search request to the Star
Wars API
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://swapi.co/api/people/?search=' + sys.argv[1]
    r = requests.get(url)
    json_obj = r.json()
    page_num = 0

    while True:
        if page_num == 0:
                print("Number of results: {}".format(json_obj.get('count')))
        else:
            r = requests.get(json_obj['next'])
            json_obj = r.json()
        results = json_obj.get('results')
        for people in results:
            print(people.get('name'))
        page_num += 1
        if json_obj['next'] is None:
            break
