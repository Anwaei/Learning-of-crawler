import requests
from bs4 import BeautifulSoup
import re

DownloadUrl = "https://movie.douban.com/top250"

def downpage(url):
	data=requests.get(url)
	data.encoding = 'utf-8'
	return data.content
	
def main():
	#print(downpage(DownloadUrl))
	url=DownloadUrl
	while 1:
		content=downpage(url)
		soup=BeautifulSoup(content,"lxml")
		titles=soup.find_all('span',class_='title',string=re.compile("^[^\s]"))
		for title in titles:
			print(title.string)
		next_page=soup.find_all('a',string="后页>")
		if next_page==[]:
			break
		else:
			url=DownloadUrl+next_page[0]['href']

if __name__=='__main__':
	main()

