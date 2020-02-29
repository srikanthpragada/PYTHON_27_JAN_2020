from bs4 import BeautifulSoup
import requests

resp = requests.get(f"http://www.srikanthtechnologies.com")
soup = BeautifulSoup(resp.text, "html.parser")

for tag in soup.find_all("img"):
    print(tag['src'])

