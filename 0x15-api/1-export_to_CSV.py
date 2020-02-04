#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys
import csv


def do_request():
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(sys.argv[1]))
    d = r.json()
    name = d.get('name')
    user_id = d.get('id')
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    d_todos = r.json()
    completed = []
    titles = []
    for index in d_todos:
        if index.get('userId') == user_id:
            titles.append(index.get('title'))
            completed.append(index.get('completed'))
    with open('{}.csv'.format(sys.argv[1]), mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for index, num in enumerate(titles):
            writer.writerow([user_id, name, completed[index], num])

if __name__ == "__main__":
    do_request()
