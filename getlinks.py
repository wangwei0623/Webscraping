from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages=set()
def getLinks(pageUrl):
	global pages
	html=urlopen("http://en.wikipedia.org"+pageUrl)
	bs0bj=BeautifulSoup(html,"lxml")
	for link in bs0bj.findAll("a",href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				#new page
				newPage=link.attrs['href']
				print(newPage)
				pages.add(newPage)
				getLinks(newPage)
getLinks("")
