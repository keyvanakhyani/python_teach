import requests

def search_books(query):
    url = "https://openlibrary.org/search.json"
    params = {
        'q': query,
        'limit': 5
    }
    response = requests.get(url,params=params)
    data = response.json()
    print(f"\n{data['numFound']} :  Book found\n")
    for book in data['docs'][:5]:
        title = book.get('title', 'untitle')
        author = book.get('author_name', ['unknown'])[0]
        year = book.get('first_publish_year', 'N/A')
        print(f"📚 {title} - {author} ({year})")
        
search_books("python programming")


