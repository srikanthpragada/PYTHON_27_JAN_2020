import requests

resp = requests.get("http://localhost:8000/hr/rest/books")
if resp.status_code == 200:
    # print(resp.text)
    # Convert array of json objects to list of dict
    books = resp.json()
    for book in books:
         print(f"{book['id']} - {book['title']} - {book['author']}")
else:
    print("Sorry! Could not get details of books!")
