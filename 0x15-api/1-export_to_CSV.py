#!/usr/bin/python3
"""Script to export data in the CSV format"""
import csv
import requests as r
import sys

"""
This script exports user information and to-do list
from a REST API and writes them to a CSV file.

Usage:
    python script.py <user_id>

Inputs:
    user_id (str): The ID of the user for whom the data will be exported.

Flow:
    1. The user ID is obtained from the command-line argument.
    2. The URL of the REST API is set.
    3. The user's information is retrieved from the API using the user ID.
    4. The username is extracted from the user's information.
    5. The user's to-do list is retrieved from the API using the user ID.
    6. A CSV file is opened for writing, named after the user ID.
    7. A CSV writer is created.
    8. For each to-do item, a row is written to the CSV file containing
    the user ID, username, completion status, and title.
Outputs:
    None. The script writes the data to a CSV file but does not '
    return any value.
"""

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    usr = r.get(url + "users/{}".format(user_id)).json()
    username = usr.get("username")
    to_do = r.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, username, elm.get("completed"),
                          elm.get("title")]) for elm in to_do]
