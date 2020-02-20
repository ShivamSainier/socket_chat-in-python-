import requests
import bs4 as bs

req=requests.get('http://quotes.toscrape.com/')
soup=bs.BeautifulSoup(req.content,'html.parser')
itemo=soup.find(class_="row")
items=soup.find_all(class_='quote')
span=[item.find(class_="text").get_text() for item in items]
for n in span:
    print(n)
