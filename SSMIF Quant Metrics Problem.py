#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Import the required packages
import pandas as pd
import pandas_datareader as web
import math
import statistics
import datetime as dt


# In[13]:


#Create a function to calculate daily returns
def Daily_Returns(stock):
    
    #Call the Adj Close index in the dataframe and find the percent changes
    return stock['Adj Close'].pct_change()

#Create a function for monthly VaR
def Monthly_VaR(ticker, confidence_level= 0.05):
    
    #Use the Datareader in order to get 2019 ticker data from Yahoo Finance
    stock = web.DataReader(ticker, 'yahoo', start = '2019-1-1', end = '2019-12-31')
    
    #Sort the values of the daily returns in ascending order
    sorted_values = Daily_Returns(stock).sort_values(ascending = True, inplace = True)
    
    #Set the new sorted Daily Returns as a variable called daily_returns and rename it
    daily_returns = Daily_Returns(stock)
    daily_returns.rename('Daily Returns', inplace=True)
    
    #Combine the stock dataframe with the new column 'Daily Returns'
    updated_stock = pd.concat([stock,daily_returns], axis = 1)
    
    #Sort the values in the dataframe by the Daily Returns 
    updated_stock.sort_values(['Daily Returns'], inplace = True, ascending = True)
    
    #Count the number of days worth of data we are using and multiply by the confidence interval
    #This gives you the number of days that will be considered as losses within that interval
    #Make sure to use int and round so it is a whole number that can be computable in the next line
    data_count = int(round((stock['Adj Close'].count()*confidence_level)))
    
    #Return daily VaR by taking the index of the count-1 since indexing starts at 0
    #You have to multiply by the square root of 21 since that is the number of trading days in a month
    monthly_VaR = (updated_stock['Daily Returns'][data_count-1]) * math.sqrt(21)
    return monthly_VaR
            
#Create a function for monthly CVaR
def Monthly_CVaR(ticker, confidence_level = 0.05):
    
    #Use the Datareader in order to get 2019 ticker data from Yahoo Finance
    stock = web.DataReader(ticker, 'yahoo', start = '2019-1-1', end = '2019-12-31')
    
    #Set the new sorted Daily Returns as a variable called daily_returns and rename it
    daily_returns = Daily_Returns(stock)
    daily_returns.rename('Daily Returns', inplace=True)
    
    #Combine the stock dataframe with the new column 'Daily Returns'
    updated_stock = pd.concat([stock,daily_returns], axis = 1)
    
    #Sort the values in the dataframe by the Daily Returns 
    updated_stock.sort_values(['Daily Returns'], inplace = True, ascending = True)
    
    #Count the number of days worth of data we are using and multiply by the confidence interval
    #This gives you the number of days that will be considered as losses within that interval
    #Make sure to use int and round so it is a whole number that can be computable in the next line
    data_count = int(round((daily_returns.count()*confidence_level)))
    
    #Find the mean of all the numbers that are less than or equal to the Monthly VaR Value
    #This is done by indexing from [0:data_count-1]
    #You have to multiply by the square root of 21 since that is the number of trading days in a month
    monthly_CVaR = statistics.mean(updated_stock['Daily Returns'][:data_count-1]) * math.sqrt(21)
    return monthly_CVaR

#Create a function for monthly volatility
def Monthly_Volatility(ticker):
    
    #Use the Datareader in order to get 2019 ticker data from Yahoo Finance
    stock = web.DataReader(ticker, 'yahoo', start = '2019-1-1', end = '2019-12-31')
    
    #Set the new sorted Daily Returns as a variable called daily_returns and rename it
    daily_returns = Daily_Returns(stock)
    daily_returns.rename('Daily Returns', inplace=True)
    
    #Combine the stock dataframe with the new column 'Daily Returns'
    updated_stock = pd.concat([stock,daily_returns], axis = 1)
    
    #Volatility is the standard deviation of the 'Daily Returns' in this case
    #Calculate the stadnard deviation of the returns with index [1:] since the first value will always be NaN
    #You have to multiply by the square root of 21 since that is the number of trading days in a month
    monthly_volatility = statistics.stdev(updated_stock['Daily Returns'][1:]) * math.sqrt(21)
    return monthly_volatility

