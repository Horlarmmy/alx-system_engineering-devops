#!/usr/bin/python3
""" Exports the data to JSON"""
import json
import requests
import sys
if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    username = user.get("username")
    todos = requests.get(url + 'todos', params={"userId": sys.argv[1]}).json()

    with open("{}.json".format(user_id), "w") as f:
        json.dump({user_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        } for task in todos]}, f)
