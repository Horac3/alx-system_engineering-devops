#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests


"""
Retrieves to-do list information for all employees from a REST API and exports it to a JSON file.

Inputs:
- url: A string representing the base URL of the REST API.
- users: A list of dictionaries containing information about the users.

Outputs:
- A JSON file named "todo_all_employees.json" containing the to-do list information for all employees.
"""

## Begin Code Snippet ##
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
