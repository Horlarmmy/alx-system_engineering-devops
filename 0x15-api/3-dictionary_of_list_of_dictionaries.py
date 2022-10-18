#!/usr/bin/python3
""" Exports the all todo data to JSON"""
import json
import requests
import sys
if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users').json()

    with open("todo_all_employees.json", "w") as f:
        json.dump({
            user.get("id"): [{
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            } for task in requests.get(url + 'todos', params={"userId": user.get("id")}).json()]
            for user in users}, f)
