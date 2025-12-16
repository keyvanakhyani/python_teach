import requests
from getpass import getpass
from urllib.parse import urljoin

def get_github_repos(username):
    
    BASE_URL = "https://api.github.com"

    endpoint = f"users/{username}/repos"
    url = urljoin(BASE_URL, endpoint)

    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        repos = response.json()
        print(f"\n{len(repos)} repository for {username}:\n")
        
        for repo in sorted(repos, key=lambda x: x['stargazers_count'], reverse=True)[:5]:
            print(f"⭐ {repo['name']}: {repo['stargazers_count']} star")
            print(f"   {repo['description'] or 'No description'}\n")
    else:
        print(f"error: {response.status_code}")

username = input("GitHub username: ")
get_github_repos(username)
