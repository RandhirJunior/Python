# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:18:39 2020

@author: Randhirs
"""

import pandas as pd
import os

## Merging multiple files into a single file.------------------------------------------------------

# Reading all files in current working directory with help of os.listdir() and it return a list, os.getcwd() get present working directory
files = [file for file in os.listdir('E:\PYTHON_ALL\Pandas\Reall_World_Problem\Sales_Data')]

# created empty dataframe called all_months_data
all_months_data = pd.DataFrame()

# Reading files list and writing into panda df and adding all df to all_months_data
for file in files:
    df = pd.read_csv("E:\PYTHON_ALL\Pandas\Reall_World_Problem\Sales_Data/"+file)
    all_months_data = pd.concat([all_months_data, df], axis =0)

# Converting and saving dataframe to csv file , Index =false means excluding index    
all_months_data.to_csv('all_data.csv', index=False)

all_data = pd.read_csv("all_data.csv")

##----------------------------------------------------------------------------------------------------

## -------------Cleaning of our data , i.e in all_data datagrame. Removing null nan all these things----
#1 Drop NAN rows

def drop_duplicates(all_data_x) :
    

    nan_df = all_data_x[all_data_x.isna().any(axis=1)]
    nan_df.head()
    
    all_data_x = all_data_x.dropna(how='all')
    
    #2 FInd 'Or' and delete it
    
    all_data_x = all_data_x[all_data_x['Order Date'].str[0:2] != 'Or']
    return all_data_x

all_data = drop_duplicates(all_data)


#------------------Adding Month Coulmn to all_data------------------------
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')

# --------------Convert Columns to correct types
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered']) # make int
all_data['Price Each'] = pd.to_numeric(all_data['Price Each']) # Make flot

#all_data.to_csv('final_data.csv', index=False)

#len(all_data)

## 1. What was the best month for sales?. How much was earned that months

# Adding sales Columns 
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

result = all_data.groupby('Month').sum()


# Plotting above on graph 
import matplotlib.pyplot as plt
x = range(1,13)
plt.title('Sales by Months')
## Labels of X and Y axis
plt.ylabel('Sales in $')
plt.xlabel('Month')

plt.bar(x, result['Sales'])
plt.xticks(x)
plt.show()

## 2. Which city had the highest number of sales

# Add city column to all_data dataframe , using apply()

def get_city(address) :
    return address.split(',')[1]
    

def get_state(address) :
    return address.split(',')[2].split(' ')[1]


#all_data['City'] = all_data['Purchase Address'].apply(lambda x : f"{get_city(x)} ({get_state(x)})") 
#all_data.head()
#all_data['Purchase Address'].apply(lambda x : get_city(x) + get_state(x ))

all_data['City'] = all_data['Purchase Address'].apply(lambda x : x.split(',')[1] + ' ('+ x.split(',')[2].split(' ')[1] + ')')


results = all_data.groupby('City').sum()

# Order is important here ,it means in same order which in Sales
cities = [city for city, df in all_data.groupby('City')]

plt.bar(cities, results['Sales'])
plt.title('Sales by Months')
## Labels of X and Y axis
plt.ylabel('Sales in $')
plt.xlabel('City Nmae')
plt.xticks(cities, rotation='vertical', size=8)
plt.show()


## 3.What time should we display advertisements to maximize likeihood of custome's buying product?.

# Coverting Oder Date from string to datetime
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])

# Grabing Hours from Oder Date
all_data['Hour'] = all_data['Order Date'].dt.hour

# Grabing Minutes from Oder Date
all_data['Minute'] = all_data['Order Date'].dt.minute


hours =  [hour for hour, df in all_data.groupby('Hour')]

plt.plot(hours, all_data.groupby(['Hour']).count())
plt.xticks(hours)
plt.grid()
plt.ylabel('Order Count')
plt.xlabel('Hours')
plt.show()

## 4. What product are most often sold togethers.
df = all_data[all_data['Order ID'].duplicated(keep=False)]

df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))

df = df[['Order ID', 'Grouped']].drop_duplicates()

from itertools import combinations
from collections import Counter

count = Counter()

for row in df['Grouped'] :
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 2)))

for key, value in count.most_common(10) :
    print(key, value)


## 5. What product sold the most?. Why do you think it sold the most
product_group = all_data.groupby('Product')  

qunatity_order = product_group.sum()['Quantity Ordered']

product = [product for product , df in product_group]

plt.bar(product,qunatity_order)
plt.xticks(product, rotation='vertical', size=8)
plt.ylabel('Qunatity Order ')
plt.xlabel('Prodcuts')
plt.show()


prices = all_data.groupby('Product').mean()['Price Each']

fig ,ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(product, qunatity_order, color='g')
ax2.plot(product,prices, 'b-')

ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered', color='g')
ax2.set_ylabel('Price ($)', color='b')
ax1.set_xticklabels(product, rotation='vertical', size=8)
plt.show()


