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

    r_films = requests.get("https://swapi.co/api/films/")
    films_obj = r_films.json().get('results')

    films_dict = {}
    for film in films_obj:
        films_dict[film.get('url')] = film.get('title')

    while True:
        if page_num == 0:
                print("Number of results: {}".format(json_obj.get('count')))
        else:
            r = requests.get(json_obj['next'])
            json_obj = r.json()
        for people in json_obj.get('results'):
            print(people.get('name'))
            for films_url in people.get('films'):
                print("\t{}".format(films_dict[films_url]))
        page_num += 1
        if json_obj['next'] is None:
            break
