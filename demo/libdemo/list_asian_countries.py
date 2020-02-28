
import requests

resp = requests.get(f"https://restcountries.eu/rest/v2/region/europe")
countries = resp.json()

for country in sorted(countries, key = lambda d: d['population'],reverse=True):
    print(f"{country['name']:50} {country['population']:12}")
