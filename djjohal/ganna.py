import requests
import bs4 as bs

req=requests.get('https://gaana.com/newrelease/hindi')
soup=bs.BeautifulSoup(req.content,'html.parser')
#table=soup.find(class_="lastend-container")
ul=soup.find(class_="content-container clearfix a-list artworkload newrelease")
items=ul.find_all(class_="album-name block_dotes _dotes pjax")
listt=[item.get_text() for item in items]
for songs in listt:
    print(songs)

