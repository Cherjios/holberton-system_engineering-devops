#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


def do_request():
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(sys.argv[1]))
    d = r.json()
    name = d.get('name')
    user_id = d.get('id')
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    d_todos = r.json()
    tasks, completed = 0, 0
    titles = []
    for index in d_todos:
        if index.get('userId') == user_id:
            tasks += 1
            if index.get('completed'):
                completed += 1
                titles.append(index.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, tasks))
    for index in titles:
        print('\t', index)

if __name__ == "__main__":
    do_request()
