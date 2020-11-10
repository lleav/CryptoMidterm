import urllib.request
import os
import time
import pandas as pd

if not os.path.exists("CMHIST_html"):
  os.mkdir("CMHIST_html")

df = pd.read_csv("parsed_filesCM/coinmarketcap_dataset.csv")

for link in df['link']:
  filename = link.replace('/currencies/', '')
  if os.path.exists("CMHIST_html/" + filename + ".html"):
    print(filename + ".html already exists.")
  else:
    print(link)
    response = urllib.request.urlopen("http://coinmarketcap.com" + link + '/historical-data/?start=20191105&end=20201105')
    html = response.read()
    f = open('CMHIST_html/' + filename + '.html', 'wb')
    f.write(html)
    f.close()
    # os.rename('deep_link_html/' + filename + 'html.temp', 'deep_link_html/' + filename + 'html')
    time.sleep(20)
