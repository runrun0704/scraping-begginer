import requests
from bs4 import BeautifulSoup

load_url = "https://news.yahoo.co.jp/categories/it"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

topic = soup.find(class_ = "sc-jGFFOr Pplqh")
for element in topic.find_all("a"):
    print(element.text)