# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 00:08:16 2020

@author: Randhirs
"""
## imported necessay liabaries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

## Reading csv file by pandas in dataframe
gas = pd.read_csv('gas_prices.csv')

## dataFrame.iloc[<ROWS INDEX RANGE> , <COLUMNS INDEX RANGE>]
#print(gas.iloc[:,0])
#print(gas.iloc[:,-1])

## To increase the Graph size
plt.figure(figsize=(8,5))

# Adding Title
plt.title('Gas price Comparision of Different Countries', fontdict={'fontweight':'bold', 'fontsize':18})



## Ploting the Graph
plt.plot(gas.iloc[:, 0], gas.iloc[:,-1] ,'r.-')
plt.plot(gas.Year, gas.Canada ,'b>-')
plt.plot(gas['Year'], gas['South Korea'], 'g.--')
plt.plot(gas.Year, gas.Australia, 'y.-')
plt.plot(gas.Year, gas.Italy, 'y*-')


"""
## Another way to plot the graph
for country in gas:
    ## to exclude year columns 
    if country != 'Year':
        plt.plot(gas.Year, gas[country], marker='.' )

"""

## Plot X and Y
plt.xlabel("Years")
plt.ylabel("Gas Prices in $")

# Xticks every three years and adding 2011 year extra
plt.xticks(gas.Year[::3].tolist()+[2011])

# To print the label
plt.legend()

# To Save the graph
plt.savefig('Gas_price_Figure.png',dpi=300)

# To plot the graph
plt.show()

