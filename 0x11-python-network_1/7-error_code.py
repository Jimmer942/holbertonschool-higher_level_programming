#! /usr/bin/python3

""" Python script that takes in a URL,
   sends a request to the URL and displays the body of the response"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    try:
        print(req.text)
    except HTTPError as e:
        print('Error code: {}'.format(req.status_code))
