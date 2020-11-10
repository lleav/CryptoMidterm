import urllib.request
from urllib.request import Request, urlopen
import os
import time 
import datetime
import pandas as pd


while True:
	for j in range(165):
		print(j)

		if not os.path.exists("coinmarket_htmls"):
			os.mkdir("coinmarket_htmls")

		if not os.path.exists("coingecko_htmls"):
			os.mkdir("coingecko_htmls")

		for i in range(1,6):
			current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
			filename = '/' + str(i) + '/'
			if os.path.exists("coinmarket_htmls" + filename + ".html"):
				print(filename + ".html already exists")
			else:
				print("downloading " + str(i))
				response = urllib.request.urlopen("http://coinmarketcap.com" + "/" + str(i) + "/")
				html = response.read()
				f = open('coinmarket_htmls/' +current_time_stamp+ str(i) + '.html', 'wb')
				f.write(html)
				f.close()
				current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
				filename = '/' + str(i) + '/'
				if os.path.exists("coingecko_htmls" + filename + ".html"):
					print(filename + ".html already exists")
				else:
					print("downloadingcg " + str(i))
					f = open('coingecko_htmls/' +current_time_stamp+ str(i) + '.html', 'wb')
					req = Request("http://www.coingecko.com/" + "/" + "en?page=" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
					html = urlopen(req).read()
					f.write(html)
					f.close()
					time.sleep(61)
		time.sleep(839)
		
	if "urllib.error.HTTPError: HTTP Error 404: Not Found":
	    time.sleep(10)
	    continue
	 #this if is for a specific error I encountered 
	 #add more statements for errors of concern, or take it out while and if statement out entirely


