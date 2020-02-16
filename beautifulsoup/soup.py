import bs4 as bs
import urllib.request

with open ('index.html') as html_file:  #to open the file in local directory
    soup=bs.BeautifulSoup(html_file,'lxml')   # convert the file
    match=soup.find('div',class_="fl_left").text   #find the attribute
print(match)
