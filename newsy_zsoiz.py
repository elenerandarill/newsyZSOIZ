import requests
from bs4 import BeautifulSoup
from pprint import pprint


url = "https://zsoiz-czyzew.pl"

r = requests.get(url)
html_src = r.text
print("Pobieram zsoiz-czyzew.pl...")

soup = BeautifulSoup(html_src, 'html.parser')
search = soup.find_all("div", class_='news-title')
# print(type(search))

print("Nagłówki aktualności ze strony https://zsoiz-czyzew.pl:")
for el in search:
    art_title = " ".join(el.a.string.split())
    art_time = " ".join(el.time.string.split())
    print(f"- {art_title}, {art_time}")

