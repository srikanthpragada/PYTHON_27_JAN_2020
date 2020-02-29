from bs4 import BeautifulSoup
import requests

resp = requests.get(f"http://www.srikanthtechnologies.com/rss.xml")
soup = BeautifulSoup(resp.text, "lxml-xml")

for item in soup.find_all("item")[:10]:
    print(item.find("title").text.strip())
    print(item.find("pubDate").text.strip())
    print('-' * 50)




