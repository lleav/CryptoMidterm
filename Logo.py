from bs4 import BeautifulSoup
import os
import glob
import pandas as pd
import time

if not os.path.exists("logo"):
	os.mkdir("logo")

df = pd.DataFrame()

for one_file_name in glob.glob("CGHIST_html/*.html"):
	print(one_file_name)
	f = open(one_file_name, encoding="utf-8")
	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()

	div = soup.find('div', {"class": "col-lg-7 col-md-7 d-flex justify-content-center flex-md-row align-middle align-items-center justify-content-md-start p-0 m-0"})
	logo = div.find('img').attrs['src']

	df = df.append({
			'name': one_file_name,
		    'logo': logo
		        	} ,ignore_index=True)
df.to_csv("logo/logo.csv")