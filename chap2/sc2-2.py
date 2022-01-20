import requests
from bs4 import BeautifulSoup

load_url = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

list_ = ["title", "h2", "li"]

for i in list_:
    print(soup.find(i).text)