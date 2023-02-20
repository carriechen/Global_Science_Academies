import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urlparse
import time
import json
from pathlib import Path

def serchLinks(url):
	'''
	Search for all the urls with http:// or https:// regx and all the <a href=""> tags
	'''
	website = urllib.request.urlopen(url)
	html = website.read()
	soup = BeautifulSoup(html,'lxml')
	#use re.findall to get all the links with http:// or https:// url
	mylinks =[]
	mylinkstext =[]
	# Find all the href links in <a > tags
	if len(soup.find('header').find('nav').find_all('a', href=True))>0:
		menueurls=soup.find('header').find('nav').find_all('a', href=True)
	elif len(soup.find('header').find_all('a', href=True))>0:
		menueurls=soup.find('header').find_all('a', href=True)
	else :
		menueurls=soup.find_all('a', href=True)
	# print(menueurls)
	for link in menueurls:
		mylinks.append(link['href'])
		mylinkstext.append(link.text)
	k=list(zip(mylinks,mylinkstext))
	return k
	
def report(url):
	'''
	Show the final results with the extension of the url
	'''
	
	jpath=urlparse(url).netloc+'.json'
	# my_file = Path(jpath)
	# if not my_file.is_file():
	# 	try:
	# 		links = serchLinks(url)
	# 		data={}
	# 		for linktxt in links:
	# 			link,txt=linktxt
	# 			data[txt]=link
	# 		with open(jpath,'w') as f:
	# 			json.dump(data, f)
	# 		return urlparse(url).netloc+'.json'
	# 	except:
	# 		print(url)
	return jpath