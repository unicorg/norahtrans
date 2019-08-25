#This is an Stock Earnings Summary Using Classes
#written by Norah Tran
#08/11/2019

#The method for this homework is to read json file and store in dictionaries.
#From dictionaries, create lists that can be used to plot graph with Matplotlib.

import json
import matplotlib
import matplotlib.pyplot as plt


#Create nested dictionary based on : stocksymbol -> stockholders
from datetime import datetime
#Create database dictionaries for investors, stocks and bonds
stock_symbol =  {}
portfolio_quantity =[]
company_name = []

def clearlist():
	graph_date.clear()
	graph_close.clear()
	
def unique(input_list): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in input_list: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list

def main():
	filepath = r"C:\temp\AllStocks.json"
	with open(filepath) as f:
		dataSet = json.load(f)
	for stock in dataSet:
		#As the AllStocks.json did not save Open,High,Low as float, I'll just keep the same veriable types from Json
		#If the stock symbol is already stored in the stock symbol database, add the stock read into the correct stock symbol using it's purchase date as the primary key
		if stock["Symbol"] in stock_symbol.keys():
			stock_symbol[stock["Symbol"]][datetime.strptime(stock['Date'], '%d-%b-%y')]= {'Open':stock["Open"], 'High':stock["High"],'Low':stock["Low"],'Close':float(stock["Close"]),'Volume':int(stock["Volume"])}
		#If the stock symbol has not been stored in the stock symbol database, add the new stock first then add its first stock
		else:
			stock_symbol.update({stock["Symbol"] : {} } )
			stock_symbol[stock["Symbol"]][datetime.strptime(stock['Date'], '%d-%b-%y')]= {'Open':stock["Open"], 'High':stock["High"],'Low':stock["Low"],'Close':float(stock["Close"]),'Volume':int(stock["Volume"])}
	

	#iterate and generate new lists to contain all stock information to create profiles
	for stock_company, stock_item in stock_symbol.items():
		stockquantity = 0;	
		for stock_data, stockinfo in stock_item.items(): 
			#graph_date.append(matplotlib.dates.date2num(stock_data))
			#Calculate the total value of the stock at close "volume * close price"
			stockquantity += stockinfo['Volume']
		portfolio_quantity.append(stockquantity)
		company_name.append(stock_company)
	print(portfolio_quantity)
	print(company_name)
	total = sum(portfolio_quantity)
	pylist = [x / total for x in portfolio_quantity]
	# Data to plot
	labels = company_name
	sizes = pylist
	colors = ['gold', 'yellowgreen', 'purple', 'lightskyblue', 'pink', 'teal','red','grey']
	# Plot
	plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
	plt.axis('equal')
	plt.show()
	



      

main()
