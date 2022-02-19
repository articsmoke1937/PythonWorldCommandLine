import bs4 as bs
import requests
import pandas as pd
import re

company = 'Facebook Inc'
filing = '10-Q'
year = 2020
quarter = 'QTR3'
#get name of all filings 
download = requests.get(f'https://www.sec.gov/Archives/edgar/full-index/{year}/{quarter}/master.idx').content
download = download.decode("utf-8").split('\n')
print(download)