import requests
from bs4 import BeautifulSoup


r = requests.get("https://zsoiz-czyzew.pl")
html_src = r.text
print("Pobieram zsoiz-czyzew.pl...")
soup = BeautifulSoup(html_src, 'lxml')
headlines = soup.find_all("div", class_='news-title')
# print(type(headlines))
news_titles = []
for head in headlines:
    alinks = head.find_all("a")
    # print(alinks)
    for link in alinks:
        news = link.text
        news_titles.append(news.strip())

print("Nagłówki aktualności ze strony https://zsoiz-czyzew.pl:")
for n in news_titles:
    print(f"-{n}")


