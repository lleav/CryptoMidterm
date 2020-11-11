from bs4 import BeautifulSoup
import os
import glob
import pandas as pd
import time

if not os.path.exists("ParsedHistDataCG"):
	os.mkdir("ParsedHistDataCG")

df = pd.DataFrame()

for one_file_name in glob.glob("CGHIST_html/*.html"):
	print(one_file_name)
	f = open(one_file_name, encoding="utf-8")
	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()


	currencies_table = soup.find("tbody")
	currency_rows =	currencies_table.find_all("tr")
	div = soup.find('div', {"class": "col-lg-7 col-md-7 d-flex justify-content-center flex-md-row align-middle align-items-center justify-content-md-start p-0 m-0"})
	logo = div.find('img').attrs['src']

	for r in currency_rows:	
		currency_columns = r.find_all("td")
		if len(currency_columns)>0:
			table_data = r.find("td")
			currency_date = r.find("th", {"class": "font-semibold text-center"}).text
			print(currency_date)
			currency_marketcap = r.find("td", {"class": "text-center"}).text
			marketcap = (currency_marketcap[1:40])
			volume = (currency_columns[1]).contents
			open_value = (currency_columns[2]).contents
			close_value = (currency_columns[3]).contents

		df = df.append({
				'name': one_file_name,
				'date': currency_date,
				'volume': volume,
				'open_val': open_value,
				'close_val': close_value,
				'marketcap': marketcap,
						} ,ignore_index=True)

		df.to_csv("ParsedHistDataCG/parsed_datahistCG.csv")

