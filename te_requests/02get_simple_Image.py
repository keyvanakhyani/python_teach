import requests

url = "https://picsum.photos/800/600"
response = requests.get(url)

if response.status_code == 200:
    with open("random_image.jpg", "wb") as f:
        f.write(response.content)

    print("image downloaded") 