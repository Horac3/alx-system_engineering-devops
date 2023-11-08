#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

"""
Exports to-do list information for a given employee ID to JSON format.

Args:
    user_id (str): The user ID representing the employee.

Example Usage:
    python script.py 1

    In this example, the script is executed with the command line
    argument "1" to specify the user ID.
    The code snippet will retrieve the user's information and
    to-do list from the API, and then write
    the data to a JSON file named "1.json".

Outputs:
    A JSON file containing the user's to-do list information.
    The file is named after the user ID and
    has the following structure:
    {
        "user_id": [
            {
                "task": "Task 1",
                "completed": true,
                "username": "John"
            },
            {
                "task": "Task 2",
                "completed": false,
                "username": "John"
            },
            ...
        ]
    }
"""

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
        