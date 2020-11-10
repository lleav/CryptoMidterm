from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("parsed_filesCG"):
	os.mkdir("parsed_filesCG")

df = pd.DataFrame()

for one_file_name in glob.glob("coingecko_htmls/*.html"):
	# one_file_name = "html_files/coinmarketcap20200929132331.html"
	print(one_file_name)
	scrape_time = os.path.basename(one_file_name).replace("coingecko","").replace(".html","")
	f = open(one_file_name, encoding="utf-8")
	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()

	currencies_table = soup.find("tbody")
	currency_rows =	currencies_table.find_all("tr")

	for r in currency_rows:	
		currency_columns = r.find_all("td")
		if len(currency_columns)>8:
			currency_price = currency_columns[3].find("span", {"class": "no-wrap"}).text.replace("$","").replace(",","")
			# print(currency_price)
			currency_name = currency_columns[2].find(("a"), {"class": "d-none d-lg-flex font-bold align-items-center justify-content-between"}, ["href"]).text.replace("\n","")
			# print(currency_name)
			currency_symbol = currency_columns[2].find(("a"), {"class": "d-lg-none font-bold"}, ["href"]).text.replace("\n","")
			# print(currency_symbol)
			currency_marketcap = (currency_columns[8]).find("span", {"class": "no-wrap"}).text.replace("$","").replace(",","")
			currency_link = currency_columns[2].find("a")["href"]
			# print(currency_link)
			currency_volume = (currency_columns[7]).find("span", {"class": "no-wrap"})
			if currency_volume:
				currency_volume = (currency_columns[7]).find("span", {"class": "no-wrap"}).text.replace("$","").replace(",","")
			else: 
				currency_volume = []	
		df = df.append({
				'time': scrape_time,
				'name': currency_name,
				'price': currency_price,
				'symbol': currency_symbol,
				'marketcap': currency_marketcap,
				'link': currency_link,
				'volume': currency_volume

						} ,ignore_index=True)

df.to_csv("parsed_filesCG/coingecko_dataset.csv")