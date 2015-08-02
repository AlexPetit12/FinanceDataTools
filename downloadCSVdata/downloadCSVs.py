#!/usr/bin/env python3

import csv
import urllib.request
import sys

path_csv_symbols = sys.argv[1] # path to csv file containing symbols
local_path_yahoo_files = sys.argv[2] # path to local directory where to save yahoo files

with open(path_csv_symbols) as file:
	reader = csv.reader(file, delimiter=";")
	next(file) # skip header
	for i, line in enumerate(reader):
		symbol = (line[0].split(",")[0]) # get symbol
		yahoo_url = "http://ichart.finance.yahoo.com/table.csv?s={}&d=3&e=23&f=2014&g=d&a=3&b=12&c=1996&ignore=.csv".format(symbol)
		try:
			urllib.request.urlretrieve(yahoo_url, "{}/{}.csv".format(local_path_yahoo_files, symbol)) # download file
		except:
			e = sys.exc_info()[0]
			print("Error: {}.".format(e))
			print("Couldn't download symbol {}.\n".format(symbol))

print("End of script")
