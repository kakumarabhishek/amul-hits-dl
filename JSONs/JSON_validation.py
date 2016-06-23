from bs4 import BeautifulSoup
import urllib
import json
import csv
import os

years = ['1976', '1979', '1981', '1981', '1982', '1983', '1986', '1987']
for year in range(1989,2017): years.append(str(year))

def parse(text):
    try:
        return json.loads(text)
    except ValueError as e:
        print('invalid json: %s' % e)
    	return None # or: raise

for year in years:
	with open((str(year) + "_advertisement_data.json"), "r") as json_file:
		return json.load(json_file)