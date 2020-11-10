from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("parsed_filesCM"):
	os.mkdir("parsed_filesCM")

df = pd.DataFrame()

for one_file_name in glob.glob("coinmarket_htmls/*.html"):
	# one_file_name = "html_files/coinmarketcap20200929132331.html"
	print(one_file_name)
	scrape_time = os.path.basename(one_file_name).replace("coinmarket","").replace(".html","")
	f = open(one_file_name, encoding="utf-8")
	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()

	currencies_table = soup.find("tbody")
	currency_rows =	currencies_table.find_all("tr")

	for r in currency_rows:	
		currency_columns = r.find_all("td")
		if len(currency_columns)>10:
			currency_price = currency_columns[3].find("a", {"class": "cmc-link"}).text.replace("$","").replace(",","")
			currency_name = currency_columns[2].find("p").text
			currency_symbol = currency_columns[2].find("p", {"class": "coin-item-symbol"}).text
			currency_marketcap = (currency_columns[6]).find("p").text
			currency_link = currency_columns[2].find("a")["href"]
			try: currency_volume = currency_columns[7].find("p", {"class": "Text-sc-1eb5slv-0 iOrfwG font_weight_500___2Lmmi"}).text
			except:
				currency_volume = currency_columns[7].find("p", {"class": "Text-sc-1eb5slv-0 hVAibX font_weight_500___2Lmmi"}).text

			df = df.append({
					'time': scrape_time,
					'name': currency_name,
					'price': currency_price,
					'symbol': currency_symbol,
					'marketcap': currency_marketcap,
					'link': currency_link,
					'volume': currency_volume

							} ,ignore_index=True)

df.to_csv("parsed_filesCM/coinmarketcap_dataset.csv")