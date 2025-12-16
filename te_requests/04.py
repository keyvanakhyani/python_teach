import requests
import time

websites = [
    "https://google.com",
    "https://github.com",
    "https://python.org"
]

def check_status(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code, response.elapsed.total_seconds()
    except requests.exceptions.RequestException as e:
        return None, str(e)

for site in websites:
    status, time_taken = check_status(site)
    if status:
        emoji = "✅" if status == 200 else "⚠️"
        print(f"{emoji} {site}: {status} ({time_taken:.2f}s)")
    else:
        print(f"❌ {site}: error - {time_taken}")

