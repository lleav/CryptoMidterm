import os
import time 
import datetime
import pandas as pd
import requests
import cloudscraper

scraper = cloudscraper.create_scraper()

if not os.path.exists("CGHIST_html"):	
	os.mkdir("CGHIST_html")

col_list = [0]
input = pd.read_csv("coinname/links.csv", usecols=col_list)
#used parsed coin names to limit requests
#if you are only interested in historical datautilize deep link here
# print(input)
for i in range(0,500):
	filename = input.iloc[i,0]
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")

	if os.path.exists("CGHIST_html" + filename + ".html"):
		print(filename + ".html already exists")
	else:
		print("downloading " + str(i))
		f = open('CGHIST_html/' + filename + '.html', 'wb')
		page = (scraper.get("https://www.coingecko.com/en/coins/" + filename+ "/historical_data/usd?end_date=2020-11-05&start_date=2019-11-05#panel").content)
		# page = requests.get("https://www.coingecko.com/en/coins/" + filename+ "/historical_data/usd")
		# response = urllib.request.urlopen("https://www.coingecko.com/en/coins/" + filename+ "/historical_data/usd")
		# html = response.read()
		f.write(page)
		f.close()
		time.sleep(30)
