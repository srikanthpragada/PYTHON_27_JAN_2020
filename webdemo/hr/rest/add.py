import requests

title = input("Enter title :")
author = input("Enter author : ")
price = input("Enter price : ")
data = {'title': title, 'author': author,'price': price}

resp = requests.post("http://localhost:8000/hr/rest/books/", data)
if resp.status_code == 200:
    print("Book added successfully!")
else:
    print("Sorry! Could not add book!")
