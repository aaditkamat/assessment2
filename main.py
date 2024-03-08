import functions_framework
import json
import requests
import pathlib
import os

# Register an HTTP function with the Functions Framework
@functions_framework.http
def get_users(request):
    if pathlib.Path('data/users.json').exists():
        with open('data/users.json', mode='r') as file:
            users_data = json.load(file)
        return users_data
    else:
        url = 'https://jsonplaceholder.typicode.com/users'
        r = requests.get(url)
        if r.status_code == 200:
            users_data = r.json()
             # Even if the data directory exists, create it again to create the JSON file 
             # from scratch
            os.makedirs('data', exist_ok=True)
            with open('data/users.json', mode='w') as file:
                json.dump(users_data, file) 
            return users_data
        else:
            print(f"Couldn't access {url} due to HTTP error with code {r.status_code}")
            return {}