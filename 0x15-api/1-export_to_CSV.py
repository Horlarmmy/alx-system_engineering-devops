#!/usr/bin/python3
""" Exports the data to CSV"""
import csv
import requests
import sys
if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    username = user.get("username")
    todos = requests.get(url + 'todos', params={"userId": sys.argv[1]}).json()

    completed = [task.get('title') for task in todos if task.get(
        'completed') is True]
    with open("{}.csv".format(user_id), 'w', newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username, task.get("completed"), task.get("title")])