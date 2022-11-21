# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 09:45:28 2022

@author: gabel
"""

import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

yf.pdr_override()

stock = input("Please enter a stock number: ")
print(stock)

year = 2020
month = 11
day = 20

start = dt.datetime(year, month, day)
now = dt.datetime.now()

df = pdr.get_data_yahoo(stock, start, now)

# ma = 50

# string_ma = "Sma_"+str(ma)

# df[string_ma] = df.iloc[:,4].rolling(window=ma).mean()

# print(df)

# df=df.iloc[ma:]
# print(df)

emasUsed = [3,5,8,10,12,15,30,40,45,50,60]
for x in emasUsed:
    ema = x
    df["Ema_"+str(ema)] = round(df.iloc[:,4].ewm(span=ema, adjust=False).mean(),2)
print(df.tail())

# pos is the position, 0 for a buy and a 1 for a sell
pos = 0
num = 0
# percent change is a list for day to day changes in and buy price and sell price.
percent_change = []

for i in df.index:
    # Takes dataframe index, looks at exopentail moving averages in the short term and long term
    cmin = min(df["Ema_3"][i], df["Ema_5"][i], df["Ema_10"][i], df["Ema_12"][i], df["Ema_15"][i])
    cmax = min(df["Ema_30"][i], df["Ema_40"][i], df["Ema_45"][i], df["Ema_50"][i], df["Ema_60"][i])
    
    # close is the adjusted price of the close
    close = df["Adj Close"][i]
    
    # If the shorter term ema's greater than longer term, then pattern is red white blue
    # and results in a buy 
    if cmin > cmax:
        print("Red White Blue")
        if pos == 0:
            # Bp = buy price and is assigned to closed, meaning it is a buy
            bp = close
            # pos = 1, meaning that it is now being held.
            pos = 1
            print("Buying now at " + str(bp))
    # If the longer term ema's are greater than the avg of the short term ema's
    # Then it is a selling point
    elif cmin < cmax:
        print("Blue White Red")
        if pos == 1:
            pos = 0
            sp = close
            print("Selling now at "+ str(sp))
            # Creating a percent change by dividing sell price by the buy price
            # then appending that to percent change list.
            pc =(sp/bp-1) * 100
            percent_change.append(pc)
    
    # Takes the adjusted close and pos number to determine if a sale is still open in 
    # the pandas dataframe and whether to sell or not.
    if num == df["Adj Close"].count()-1 and pos == 1:
        pos = 0
        sp = close
        print("Selling now at "+ str(sp))
        pc =(sp/bp-1) * 100
        percent_change.append(pc)
        
    num += 1
print(percent_change)
# Gains in terms of percentage
gains = 0
#number of gains
ng = 0
# Losses in terms of percentage
losses = 0
# number of losses
nl = 0
# Total Return
totalR = 1

#if the percent change is positive, gains and number of gains is increased by 1
for i in percent_change:
    if i > 0:
        gains += 1
        ng += 1
    else:
        losses += 1
        nl += 1
    totalR = totalR*((i/100)+1)
    
totalR = round((totalR-1)* 100, 2)

if ng> 0:
    avgGain = gains / ng
    maxR = str(max(percent_change))
else:
    avgGain = 0
    # Max return will be undefined to there isn't any gains
    maxR ="undefined"
    
if nl > 0:
    avgLoss = losses / nl
    maxL = str(min(percent_change))
    ratio = str(-avgGain / avgLoss)
else:
    avgLoss = 0
    maxL = "undefined"
    ratio = "inf"
    
if (ng > 0 or nl > 0):
    battlingAvg =  ng / (ng + nl)
else:
    battlingAvg = 0
    
print()
print("Results for "+ stock +" going back to "+str(df.index[0])+", Sample size: "+str(ng+nl)+" trades")
print("EMAs used: "+str(emasUsed))
print("Batting Avg: "+ str(battlingAvg))
print("Gain/loss ratio: "+ ratio)
print("Average Gain: "+ str(avgGain))
print("Average Loss: "+ str(avgLoss))
print("Max Return: "+ maxR)
print("Max Loss: "+ maxL)
print("Total return over "+str(ng+nl)+ " trades: "+ str(totalR)+"%" )
#print("Example return Simulating "+str(n)+ " trades: "+ str(nReturn)+"%" )
print()
# numH = 0
# numC = 0
# for i in df.index:
#     if (df["Adj Close"][i] > df[string_ma][i]):
#         print("The close is higher")
#         numH += 1
#     else:
#         print("The close is lower")
#         numC += 1        
# print("The close is higher "+str(numH)+" times")
# print("The close is lower "+ str(numC) + " times")