#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests

from bs4 import BeautifulSoup

#import os
#os.environ.setdefault("DJANGO_SETTINGS_MODULE","bot.settings")
#import django
#django.setup()
def prostitution_support():
	req=requests.get('https://www.women1366.kr/_sub03/sub03_01c.html')
	html=req.text
	soup=BeautifulSoup(html,'html.parser')
	supports=soup.select('div.page > table')
	#print(len(supports))
	table=supports[1]

	tbody=table.find('tbody')
	trs=tbody.find_all('tr')

	data=""
	for tr in trs:
		nation=tr.find('th')
		data+=("*"+nation.text+"  ")
		call=tr.find('td')
		data+=(call.text+"\n")
	return data
	

def domestic_support():
	req=requests.get('https://www.women1366.kr/_sub03/sub03_01a.html')
	html=req.text
	soup=BeautifulSoup(html,'html.parser')
	supports=soup.select('table > tbody > tr')

	data=""
	for support in supports:
		th=support.find('th')
		data+=("*"+th.text+"\n")
		td=support.find('td')
		data+=(td.text+"\n")
	return data
	
def panre_crawler(input_search):
	url='https://casenote.kr/search/'
	#panre_dict=OrederDict()
	
	data=''
	for page in range(1,3):
		params={
			'q':input_search,
			'p':page,
		}
		req=requests.get(url,params=params,timeout=100)
		html=req.text
		soup=BeautifulSoup(html,'html.parser')
		title_list=soup.select('.casename')

		for title in title_list:
			data+=title.text+'\n'+'https://casenote.kr'+title['href']+'\n\n'

	return data

def parse_domestic(area):	
	req=requests.get('https://www.women1366.kr/_sub03/sub03_02b.html')
	html=req.text
	soup=BeautifulSoup(html,'html.parser')
	places=soup.select('table > tbody > tr')

	for place in places:
		if place.find('th') is not None:
			th=place.find_all('th')
		
			if th[0].text=='서울':
				seoul_firstcount=places.index(place)
	
			
			if th[0].text=='부산':
				busan_firstcount=places.index(place)
	
			if th[0].text=='대구':
				daegu_firstcount=places.index(place)
		
			if th[0].text=='인천':
				incheon_firstcount=places.index(place)

			if th[0].text=='광주':
				gwangju_firstcount=places.index(place)

			if th[0].text=='대전':
				daejeon_firstcount=places.index(place)
			if th[0].text=='울산':
				ulsan_firstcount=places.index(place)
			if th[0].text=='경기':
				geonggi_firstcount=places.index(place)

			if th[0].text=='강원':
				gangwon_firstcount=places.index(place)

			if th[0].text=='충북':
				chungbook_firstcount=places.index(place)
			if th[0].text=='충남':
				chungnam_firstcount=places.index(place)
			if th[0].text=='전북':
				jeonbook_firstcount=places.index(place)
			if th[0].text=='전남':
				jeonnam_firstcount=places.index(place)
			if th[0].text=='경북':
				keongbook_firstcount=places.index(place)
			if th[0].text=='경남':
				keongnam_firstcount=places.index(place)
			if th[0].text=='제주':
				jeju_firstcount=places.index(place)
			if th[0].text=='세종':
				sejong_firstcount=places.index(place)
	if area=='서울':
		places=places[seoul_firstcount:busan_firstcount]	
	elif area=='부산':
		places=places[busan_firstcount:daegu_firstcount]	
	elif area=='대구':
		places=places[daegu_firstcount:incheon_firstcount]	
	elif area=='인천':
		places=places[incheon_firstcount:gwangju_firstcount]	
	elif area=='광주':
		places=places[gwangju_firstcount:daejeon_firstcount]	
	elif area=='대전':
		places=places[daejeon_firstcount:ulsan_firstcount]	
	elif area=='울산':
		places=places[ulsan_firstcount:geonggi_firstcount]	
	elif area=='경기':
		places=places[geonggi_firstcount:gangwon_firstcount]	
	elif area=='강원':
		places=places[gangwon_firstcount:chungbook_firstcount]	
	elif area=='충북':
		places=places[chungbook_firstcount:chungnam_firstcount]	
	elif area=='충남':
		places=places[chungnam_firstcount:jeonbook_firstcount]	
	elif area=='전북':
		places=places[jeonbook_firstcount:jeonnam_firstcount]	
	elif area=='전남':
		places=places[jeonnam_firstcount:keongbook_firstcount]	
	elif area=='경북':
		places=places[keongbook_firstcount:keongnam_firstcount]	
	elif area=='경남':
		places=places[keongnam_firstcount:jeju_firstcount]	
	elif area=='제주':
		places=places[jeju_firstcount:sejong_firstcount]	
	elif area=='세종':
		places=places[sejong_firstcount:]	
	
	else:
		data='입력 가능한 지역만 검색해주세요.'
		return data



	data=''
	for place in places:
		aboutPlace=place.find_all('td')
		placeName=aboutPlace[0].text
		placeAddress=aboutPlace[1].text
		placePhone=aboutPlace[2].text
		data+=('*'+placeName+'\n'+placeAddress+'\n'+placePhone+'\n')
		

	return data	

def parse_sex(area):	
	req=requests.get('https://www.women1366.kr/_sub03/sub03_02c.html')
	html=req.text
	soup=BeautifulSoup(html,'html.parser')
	places=soup.select('table > tbody > tr')

	for place in places:
		if place.find('th') is not None:
			th=place.find_all('th')
		
			if th[0].text=='서울':
				seoul_firstcount=places.index(place)

			if th[0].text=='부산':
				busan_firstcount=places.index(place)
			if th[0].text=='대구':
				daegu_firstcount=places.index(place)
			if th[0].text=='인천':
				incheon_firstcount=places.index(place)
			if th[0].text=='광주':
				gwangju_firstcount=places.index(place)

			if th[0].text=='대전':
				daejeon_firstcount=places.index(place)
			if th[0].get_text()=='울산':
				ulsan_firstcount=places.index(place)
				print(ulsan_firstcount)
			if th[0].text=='세종':
				sejong_firstcount=places.index(place)
			if th[0].text=='경기':
				geonggi_firstcount=places.index(place)

			if th[0].text=='강원':
				gangwon_firstcount=places.index(place)

			if th[0].text=='충북':
				chungbook_firstcount=places.index(place)
			if th[0].text=='충남':
				chungnam_firstcount=places.index(place)
			if th[0].text=='전북':
				jeonbook_firstcount=places.index(place)
			if th[0].text=='전남':
				jeonnam_firstcount=places.index(place)
			if th[0].text=='경북':
				keongbook_firstcount=places.index(place)
			if th[0].text=='경남':
				keongnam_firstcount=places.index(place)
			if th[0].text=='제주':
				jeju_firstcount=places.index(place)
		
	if area=='서울':
		places=places[seoul_firstcount:busan_firstcount]	
	elif area=='부산':
		places=places[busan_firstcount:daegu_firstcount]	
	elif area=='대구':
		places=places[daegu_firstcount:incheon_firstcount]	
	elif area=='인천':
		places=places[incheon_firstcount:gwangju_firstcount]	
	elif area=='광주':
		places=places[gwangju_firstcount:daejeon_firstcount]	
#	if area=='대전':
#		places=places[daejeon_firstcount:ulsan_firstcount]	
#	if area=='울산':
#		places=places[ulsan_firstcount:sejong_firstcount]	
#	if area=='세종':
#		places=places[sejong_firstcount:geonggi_firstcount]	
#	if area=='경기':
#		places=places[geonggi_firstcount:gangwon_firstcount]	
#	if area=='강원':
#		places=places[gangwon_firstcount:chungbook_firstcount]	
#	if area=='충북':
#		places=places[chungbook_firstcount:chungnam_firstcount]	
#	
#	if area=='충남':
#		places=places[chungnam_firstcount:jeonbook_firstcount]	
#	if area=='전북':
#		places=places[jeonbook_firstcount:jeonnam_firstcount]	
#	if area=='전남':
#		places=places[jeonnam_firstcount:keongbook_firstcount]	
#	if area=='경북':
#		places=places[keongbook_firstcount:keongnam_firstcount]	
#	if area=='경남':
#		places=places[keongnam_firstcount:jeju_firstcount]	
#	if area=='제주':
#		places=places[jeju_firstcount:]		

	else:
		data='입력 가능한 지역만 검색해주세요.'
		return data

	data=''
	for place in places:
		aboutPlace=place.find_all('td')
		placeName=aboutPlace[0].text
		placeAddress=aboutPlace[1].text
		placePhone=aboutPlace[2].text
		data+=('*'+placeName+'\n'+placeAddress+'\n'+placePhone+'\n')
		

	return data	

		

if __name__=='__main__':
	result=panre_crawler('성폭력')
	print(result)
#	parse_domestic()
