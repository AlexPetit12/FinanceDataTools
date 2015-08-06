#!/usr/bin/python
# -*- coding: utf-8 -*-
# retrieving_data.py
from __future__ import print_function
import pandas as pd
import MySQLdb as mdb
if __name__ == "__main__":
# Connect to the MySQL instance
    db_host = 'localhost'
    db_user = 'fred'
    db_pass = 'a1234567'
    db_name = 'PetitMorinTrading'
    con = mdb.connect(db_host, db_user, db_pass, db_name)
    # Select all of the historic Google adjusted close data
    sql = """SELECT dp.PRICE_DATE, dp.ADJUSTED_CLOSE
    FROM SYMBOL AS sym
    INNER JOIN DAILY_PRICE AS dp
    ON dp.SYMBOL_ID = sym.ID
    WHERE sym.TICKER = 'GOOG'
    ORDER BY dp.PRICE_DATE ASC;"""
    # Create a pandas dataframe from the SQL query
    goog = pd.read_sql_query(sql, con=con, index_col='PRICE_DATE')
    # Output the dataframe tail
    print(goog.tail())