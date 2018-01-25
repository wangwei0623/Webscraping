from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs0bj=BeautifulSoup(html)

namelist=bs0bj.findAll("span",{"class":"green"})
for name in namelist:
    print (name.get_text())
