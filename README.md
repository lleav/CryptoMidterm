# Cryptocurrency Downloader and Parser

## Installation
Install manually

1.  Download the github repository
2.  Copy everything in the github repository to a folder.

## Dependencies
These programs utilize urllib.request, pandas, beautifulsoup4, and cloudscraper. All can be installed using pip.
`pip install beautifulsoup4 pandas urllib3 cloudscraper`
## Usage

Main Programs (Current Data)

1. To begin scraping current data from both sites Run CryptoDownloader.py using Python
 `python3 CryptoDownloader.py`
2. Wait for all of the .html files to finish downloading. (The program is set to run in 15 minute intervals for about 50 hours and can be adjusted by adjusting the time.sleep() and range() functions in the CryptoDownloader program.)
3. You will see the following terminal response (downloading 1-5 and downloadingcg 1-5) for each time interval 0 through n.
`0`
`downloading 1`
`downloadingcg 1`
`downloading 2`
`downloadingcg 2`
`downloading 3`
`downloadingcg 3`
`downloading 4`
`downloadingcg 4`
`downloading 5`
`downloadingcg5`
https://photos.google.com/photo/AF1QipNc0inHmXzoO8bZUZv6yGNzN4Gva3aN_5gPDQJ9
4. After downloading all of the desired data run CoinGeckoParser.py and CoinMarketParser.py to parse the data.
`python3 CoinGeckoParser.py`
`python3 CoinMarketParser.py`
5. You will see the following terminal response(s) for each html. Where the number after the \ is the scrape time (your scrape time will be different).
`coingecko_htmls\202011092231531.html`
`coingecko_htmls\202011092232562.html`
`coingecko_htmls\202011092233583.html`
https://photos.google.com/photo/AF1QipPQH9Uv0xjysYm4rAw3iL049NmFsnQ0OsxkVrHL
`coinmarket_htmls\202011092231531.html`
`coinmarket_htmls\202011092232552.html`
`coinmarket_htmls\202011092233583.html`
https://photos.google.com/photo/AF1QipOA4Tm5l-bW_O9abxha53kqbrWBubkFeYZkeHRD
6. Wait until the parsing programs finish running entirely. This is important as the data frames are converted to .csv files at the very end of the program script. 
7. When the programs are done you will find your parsed data in two separate .csv files consisting of the link, market cap, name, price, symbol, time, and volume. The csv files will be titled coinmarketcap_dataset.csv and coingecko_dataset.csv respectively and will be in separate directories titled parsed_filesCG and parsed_filesCM.
8. Graphic analysis of this data was done using excel.

Secondary Programs (Logos and Historical Data)
1. To download the Logos run the program Logo.py.
`python3 Logo.py`
2. After the program finishes you will find the logos in a .csv named "logo.csv" in a directory named "logo".
 3. To scrape the historical data for each/any of the 500 coins first create a directory named coinname.
 4. Inside the coinname directory create a .csv titled links containing the data in the link column for the coins you are interested in (the link column is located in coingecko_dataset.csv and coinmarketcap_dataset.csv).
 5. Now run HistDownloaderCG.py and HistDownloaderCM.py to download the htmls containing the historical data.
`python3 HistDownloaderCG.py`
`python3 HistDownloaderCM.py`
6. The resulting html files will be located in folders titled CMHIST_html and CGHIST_html.
7. To parse the historical data for CoinGecko run CGHIST_parser.py.
`python3 CGHIST_parser.py` 
8.  After the program finishes parsing the historical data the name, date, open, close, marketcap, and volume for each coin and date will be located in the directory ParsedHistDataCG in a csv titled parsed_datahistCG.csv.

## Limitations
1. The program CryptoDownloader.py is susceptible to timeout/internet connection errors. I have used an If "error__" continue statement to prevent a particular error, feel free to repeat this structure for other errors of concern.
2. Due to time constraints there is not a historical parser built for CoinMarketCap's historical data. It could be made with roughly the same methodology. (create a dataframe with pandas, for each html in CMHIST_html read the html with bs4 html parser, find the tbody, iterate across all tr's, collect the td of interest in each tr, append the dataframe and save as a csv)
 ## License
Copyright 2020 Lee Leavitt

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


> Written with [StackEdit](https://stackedit.io/).
