import requests
import json

def create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    data = {
        'title': 'my test post',
        'body': 'this is a test post',
        'userId': 1
    }
    
    # way 1: JSON
    # response = requests.post(url, json=data)
    
    # way 2: Form data
    response = requests.post(url, data=data)
    
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

create_post()