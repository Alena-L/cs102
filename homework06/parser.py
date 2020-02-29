import requests
from bs4 import BeautifulSoup

r = requests.get("https://news.ycombinator.com/")
page = BeautifulSoup(r.text, 'html.parser')
print(page.prettify())
#print(page.get_text())
#author = page.find('a',{ 'class' : 'hnuser' }).text
#print(author)

