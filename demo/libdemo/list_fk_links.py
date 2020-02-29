from bs4 import BeautifulSoup
import requests

resp = requests.get(f"https://www.flipkart.com")
soup = BeautifulSoup(resp.text, "html.parser")

for tag in soup.find_all("a"):
    print(tag['href'])

