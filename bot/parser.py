import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","bot.settings")
import django
django.setup()

def parse_domestic():	
	req=requests.get('https://www.women1366.kr/_sub03/sub03_02b.html')
	html=req.text
	soup=BeautifulSoup(html,'html.parser')
	places=soup.select('table > tbody > tr')

	data=''
	for place in places:
		aboutPlace=place.find_all('td')
		placeName=aboutPlace[0].text
		placeAddress=aboutPlace[1].text
		placePhone=aboutPlace[2].text
		data+=('*'+placeName+'\n'+placeAddress+'\n'+placePhone+'\n')

	return data	

if __name__=='__main__':
	result=parse_domestic()
  	print(result)
