#!/usr/bin/python3

"""Python script that takes in a string
   and sends a search request to the Star Wars API"""

import requests
import sys

if __name__ == "__main__":
    url = "https://swapi.co/api/people/?search="
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    url = url+q
    req = requests.get(url)
    jsondic = req.json()
    results = jsondic['results']
    print("Number of results: {}".format(jsondic['count']))
    for i in results:
        print("{}".format(i['name']))
