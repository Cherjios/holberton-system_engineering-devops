#!/usr/bin/python3
"""Export data in JSON format"""
import json
import requests
import sys


def do_request():
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    users = r.json()
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = r.json()
    dic = {str(d.get('id')): [{'username': d.get('username'),
                               'task': i.get('title'), 'completed':
                               i.get('completed')}
                              for i in tasks
                              if i.get('userId') == d.get('id')]
           for d in users}
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(dic, json_file)

if __name__ == "__main__":
    do_request()
