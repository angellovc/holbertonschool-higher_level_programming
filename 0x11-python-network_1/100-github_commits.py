#!/usr/bin/python3
""" list 10 commits (from the most recent to oldest) of the repository """
import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner,
        repo
    )
    response = requests.get(url)
    commits = response.json()[:10]
    for commit in commits:
        id = commit.get('sha')
        name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(id, name))
