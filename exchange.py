#! /usr/bin/env python3

import urllib.request
import re
from html.parser import HTMLParser
import sys
from urllib.error import URLError, HTTPError

list = []

class myParser(HTMLParser):

	def __init__(self):
		self.tag = 0
		HTMLParser.__init__(self)

	def handle_starttag(self, tag, attrs):

		if tag == 'td':
			for (key, value) in attrs:
				if key == 'class' and value == 'hsbcAlign06':
					self.tag = self.tag + 1

	def handle_endtag(self, tag):
		if tag == 'tr':
			self.tag = 0
		if tag == 'a':
			self.tag = 0

	def handle_data(self, data):
		if self.tag == 3 or self.tag == 4:
			try:
			    number = float(data)
			except ValueError:
				pass
			else:
				list.append(data)

def getdata():

	fp = open("/var/www/html/rates/rates.txt", "w", encoding= 'utf-8')

	demo = myParser()
	url = "https://www.personal.hsbc.com.hk/1/2/chinese/hk/investments/mkt-info/fcy/rates?pwscmd=cmd_init"
	try:
		html = urllib.request.urlopen(url)
	except HTTPError as e:
		print (i, ': ', e,)
	except URLError as e:
		print (i, 'err: ', e)
	else:
		data = html.read().decode("utf-8")
		demo.feed(data)

	for item in list:
		fp.write(item+'\r\n')

	fp.close()

getdata()
