#!/usr/bin/python3
""" Python script that takes 2 arguments in order to solve this challenge """
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[1]
    url = "https://api.github.com/repos/"
    url = url + owner + "/" + repo + "/commits"
    req = requests.get(url)
    jsondic = req.json()
    count = 1
    for i in jsondic:
        print("{}: {}".format(i['sha'], i['commit']['author']['name']))
        count += 1
        if count == 10:
            break
