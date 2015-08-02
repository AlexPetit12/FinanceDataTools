#!/usr/bin/env python3

"""
This scripts parses a csv file containing symbols and then
uses yahoo to fetch historical data in csv format.

This script needs 4 arguments:
   1. path to csv file containing the symbols
   2. path where the historical data files will be saved
   3. beginning year
   4. ending year

Example to run the script: ./downloadsCSV SNP500symbols.csv ~/Desktop/yahoodata 1996 2015
"""

import csv
import sys
import urllib.request

path_csv_symbols = sys.argv[1] # path to csv file containing symbols
local_path_yahoo_files = sys.argv[2] # path to local directory where to save yahoo files
year_begin = sys.argv[3]
year_end = sys.argv[4]

if local_path_yahoo_files[-1] == "/":
	local_path_yahoo_files = local_path_yahoo_files[:-1] # remove trailing slash

with open(path_csv_symbols) as file:
	reader = csv.reader(file, delimiter=";")
	next(file) # skip header
	for i, line in enumerate(reader):
		symbol = (line[0].split(",")[0]) # get symbol
		yahoo_url = "http://ichart.finance.yahoo.com/table.csv?s={}&d=3&e=23&f={}&g=d&a=3&b=12&c={}&ignore=.csv".format(symbol, year_end, year_begin)
		try:
			urllib.request.urlretrieve(yahoo_url, "{}/{}.csv".format(local_path_yahoo_files, symbol)) # download file
		except:
			e = sys.exc_info()[0]
			print("Error: {}.".format(e))
			print("Couldn't download symbol {}.\n".format(symbol))

print("End of script")
