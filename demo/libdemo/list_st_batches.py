from bs4 import BeautifulSoup
import requests

resp = requests.get(f"http://www.srikanthtechnologies.com")
soup = BeautifulSoup(resp.text, "html.parser")

table = soup.find("table", {"id": 'ctl00_ContentPlaceHolder1_GridView2'})

for row in table.find_all("tr")[1:]: # ignore first row as it contains headings
    cols = row.find_all("td")
    print(f"{cols[0].text:30} {cols[2].text}")



