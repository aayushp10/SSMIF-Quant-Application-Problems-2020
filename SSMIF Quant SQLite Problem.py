#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd 
import pandas_datareader as web
import math
import statistics
import datetime as dt
import sqlite3
conn = sqlite3.connect('SSMIF.db')
drop_statement = "DROP TABLE IF EXISTS Stock_Data"
c = conn.cursor()
c.execute(drop_statement)
c.execute("""CREATE TABLE "Stock_Data" (
            "Timestamp" INTEGER NOT NULL,
            "Open" DECIMAL(10, 2),
            "High" DECIMAL(10, 2),
            "Low" DECIMAL(10, 2),
            "Close" DECIMAL(10, 2),
            "Adj_Close" DECIMAL(10, 2)
        );""")
conn.commit()
conn.close()


# In[32]:


def Fill_Table(ticker):
    
    #Connect to SSMIF.db
    conn = sqlite3.connect('SSMIF.db')
    c = conn.cursor()
    
    #Use pandas Datareader to get the stock data from the 2019 year from Yahoo Finance
    stock = web.DataReader(ticker, 'yahoo', start = '2019-1-1', end = '2019-12-31')
    
    #Loop through the stock data in order to fill the table
    for index, data in stock.iterrows():
        
        #Create a time stamp for the index date
        timestamp = index.timestamp()
        
        #Use an insert statement with the different variables that are going to be used in the table
        insert_statement = """INSERT INTO Stock_Data (Timestamp, Open, High, Low, Close, Adj_Close) 
        VALUES (?, ?, ?, ?, ?, ?);"""
        stock = (timestamp, data['Open'], data['High'], data['Low'], data['Close'], data['Adj Close'])
        
        #Execute the insert statement for the stock data
        c.execute(insert_statement, stock)
    
    #Commit and close the connection to the SSMIF.db
    conn.commit()
    conn.close()


# In[33]:


def Daily_Returns(adj_close_values):
    #Create an empty list for percent changes
    daily_returns = []

    #Loop through adjusted close values from the first index
    #This prevents an error since you cannot perform a calculation using index zero's value
    for i in (list(range(1, len(adj_close_values)))):
        
        #Calculate percent change for the daily returns using the formula for percent change
        daily_returns.append((adj_close_values[i]-adj_close_values[i-1])/adj_close_values[i-1])

    return daily_returns


# In[34]:


def Monthly_VaR(confidence_level = 0.05):
    
    #Connect to ssmif.db
    conn = sqlite3.connect('SSMIF.db')
    
    #Get the values that represent the rows
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
   
    #Use a select statement to get the Adjusted Close Data
    select_statement = "SELECT Adj_Close FROM Stock_Data"
    c.execute(select_statement)
    
    #Fetch stock data from the select statement
    stock_data = c.fetchall()
    
    #Close the connection
    conn.close()

    #Get the daily returns stock data using the function
    daily_returns = Daily_Returns(stock_data)
    
    #Sort the values for daily returns in ascending order
    daily_returns.sort()
    
    #Find the cutoff daily return value for the daily returns based on the confidence level
    #Make sure to use int and round so it can be used to calculate things in the next step
    
    data_count = round(int(confidence_level*len(daily_returns)))
    
    #Calculate monthly VaR using the data_count value and multiply by the square root of 21
    #This is done because there are 21 trading days in the month
    monthly_VaR = daily_returns[data_count - 1] * math.sqrt(21)
    return monthly_VaR

