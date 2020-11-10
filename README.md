# Cryptocurrency Downloader and Parser

## Installation
Install manually

1.  Download the github repository
2.  Copy everything in the github repository to a folder.
3. This program utilizes urllib.request, pandas, and beautifulsoup4. All can be installed using pip.
## Usage

Main Programs (Current Data)

1. Run CryptoDownloader.py using Python
2. `python3 CryptoDownloader.py`
3. Wait for all of the files to finish downloading. (The program is set to run in 15 minute intervals for about 50 hours and can be adjusted by adjusting the time.sleep() and range() functions in the CryptoDownloader program.)
4. You will see the following terminal response (downloading 1-5 and downloadingcg 1-5) for each time interval 0 through n.
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
5. After downloading all of the desired data run CoinGeckoParser.py and CoinMarketParser.py.
`python3 CoinGeckoParser.py`
`python3 CoinMarketParser.py`
6. You will see the following terminal response(s) for each html. Where the number after the \ is the scrape time.
`coingecko_htmls\202011092231531.html`
`coingecko_htmls\202011092232562.html`
`coingecko_htmls\202011092233583.html`
https://photos.google.com/photo/AF1QipPQH9Uv0xjysYm4rAw3iL049NmFsnQ0OsxkVrHL
`coinmarket_htmls\202011092231531.html`
`coinmarket_htmls\202011092232552.html`
`coinmarket_htmls\202011092233583.html`
https://photos.google.com/photo/AF1QipOA4Tm5l-bW_O9abxha53kqbrWBubkFeYZkeHRD
7. Wait until the parsing programs finish running entirely. This is important as the data frame is converted to a .csv file at the very end of the program script. 
8. When the programs are done you will find your parsed data in two separate .csv file's consisting of the link, market cap, name, price, symbol, time, and volume. The csv files will be titled coinmarketcap_dataset.csv and coingecko_dataset.csv respectively and will be in separate directories titled parsed_filesCG and parsed_filesCM.

Secondary Programs (Historical Data)

 1. There are also two programs included that scrape the htmls containing the historical data for each of the 500 coins.
 2. Download cloudscraper using pip.
 3. To scrape the htmls create a directory named coinname and inside create a .csv titled links containing the data in the link column (located in coingecko_dataset.csv and coinmarketcap_dataset.csv) for the coins you are interested in.
 4. Now run HistDownloaderCG.py and HistDownloaderCM.py.
`python3 HistDownloaderCG.py`
`python3 HistDownloaderCM.py`
5. The resulting html files will be located in folders titled CMHIST_html and CGHIST_html.

## Limitations
The program CryptoDownloader.py is susceptible to timeout errors and internet connection errors. I have used an If "error__" continue statement to prevent a particular error, feel free to repeat this structure for other errors of concern.
 ## License
 Copyright (C) 2012 Lee Leavitt. MIT License.


> Written with [StackEdit](https://stackedit.io/).
"# CryptoMidterm" 
