# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 14:59:00 2022

@author: gabel
"""

import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
from tkinter import Tk
from tkinter.filedialog import askopenfilename



yf.pdr_override() # <== that's all it takes :-)
start =dt.datetime(2017,12,1)
now = dt.datetime.now()

# root = Tk()
# ftypes = [(".xlsm","*.xlsx",".xls")]
# ttl  = "Title"
# dir1 = 'C:\\'
# filePath = askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl)
filePath=r"C:\Users\gabel\Downloads\Thony Programs\RichardStocks.xlsx"


stocklist = pd.read_excel(filePath)
stocklist=stocklist.head()
#print(stocklist)

exportList= pd.DataFrame(columns=['Stock', "RS_Rating", "50 Day MA", "150 Day Ma", "200 Day MA", "52 Week Low", "52 week High"])


for i in stocklist.index:
	stock=str(stocklist["Symbol"][i])
	RS_Rating=stocklist["RS Rating"][i]
	try:
		df = pdr.get_data_yahoo(stock, start, now)
        
        sma_used = [50,150,200]
        for x in sma_used:
            sma = x
            df["Sma_" + str(sma)] = round(df.iloc[:4].rolling(window=sma).mean(), 2)
            
        current_close = df["Adj Close"][-1]
        moving_average_50 = df["SMA_50"][-1]
        moving_average_150 = df["SMA_150"][-1]
        moving_average_200 = df["SMA_200"][-1]
        low_of_52week = min(df['Adj Close'][-260:])
        high_of_52week = max(df['Adj Close'][-260:])
        
        try:
            moving_average_200_month = df["Sma_200"][-20]
        except Expection:
            moving_average_200_month = 0


		print("Checking "+stock+".....")

		#Condition 1: Current Price > 150 SMA and > 200 SMA
        if current_close > moving_average_150 and current_close > moving_average_200:
            condition_1 = True
        else:
            condition_1 = False
		#Condition 2: 150 SMA and > 200 SMA
        if moving_average_150 > moving_average_200:
            condition_2 = True
        else:
            condition_2 = False
		#Condition 3: 200 SMA trending up for at least 1 month (ideally 4-5 months)
        if moving_average_200 > moving_average_200_month:
            condition_3 = True
        else:
            condition_3 = False
		#Condition 4: 50 SMA> 150 SMA and 50 SMA> 200 SMA
        if moving_average_50 > moving_average_150 and moving_average_50 > moving_average_200:
            condition_4 = True
        else:
            condition_4 = False
		#Condition 5: Current Price > 50 SMA
        if current_close > moving_average_50:
            condition_5 = True
        else:
            condition_5 = False
		#Condition 6: Current Price is at least 30% above 52 week low (Many of the best are up 100-300% before coming out of consolidation)
		if current_close > (1.3)*(low_of_52week):
            condition_6 = True
        else:
            condition_6 = False
        #Condition 7: Current Price is within 25% of 52 week high
        if current_close >= (.75 * high_of_52week):
            condition_7 = True
        else:
            condition_7 = False
		#Condition 8: IBD RS rating >70 and the higher the better
		if RS_Rating > 70:
            condition_8 = True
        else:
            condition_8 = False
            
        if (condition_1 and condition_2 and condition_3 and condition_4 and condition_5 and condition_6 and condition_7 and condition_8):
    		exportList = exportList.append({'Stock': stock, "RS_Rating": RS_Rating, "50 Day MA": moving_average_50, "150 Day Ma": moving_average_150, "200 Day MA": moving_average_200, "52 Week Low": low_of_52week, "52 week High": high_of_52week}, ignore_index=True)
	
	except Exception:
		print("No data on "+stock)

print(exportList)