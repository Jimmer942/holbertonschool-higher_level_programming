#!/usr/bin/python3

"""  Python script that takes in a URL, sends a request to the URL and displays
     the body of the response. """

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': ""}
    if len(sys.argv) > 1:
        data['q'] = sys.argv[1]
    req = requests.post(url, data)
    try:
        jsondic = req.json()
        try:
            print("[{}] {}".format(jsondic['id'], jsondic['name']))
        except:
            print("No result")
    except:
        print("Not a valid JSON")
