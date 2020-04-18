# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:19:46 2020

@author: Randhirs

pd.loc[rows:columns]
"""

import pandas as pd

fifa = pd.read_csv('fifa_data.csv')

##--------------------------pd.loc[]----------------------------------------

## pd.loc[rows,columns] method in pandas

## Zero row and all columns
fifa.loc[0,:]

## loc is iclusive in both side, here it take 0 to 2 rows and all columns
fifa.loc[0:2, :]

## all rows and all columns from ID to Club
sample_data = fifa.loc[:, 'ID':'Club']

## want rows which have fifa.Name=='Neymar Jr' and all columns :
fifa[fifa.Name=='Neymar Jr']

fifa.loc[fifa.Name=='Neymar Jr', :]

##------------------------------pd.iloc[]-----here i stand for integer-------------------------------------

## all rows and columns of index 1,2 and 3
fifa.iloc[:, [1,2,3]]

## using range in columns .i.e. 0:4
## iloc[] doecn't take last values in range .i.e here it gives columns from 0 to 3

fifa.iloc[:, 0:4]

## range 0 to 4
list(range(0,4))

## rows 0 to 3 and asll co,umns
fifa.iloc[0:3, :]

## it print rows from 0 to 1 and all columns 
fifa[0:2]

fifa.iloc[0:2 , :]

#---------------------------------READING Different dataset-------------------------------------------
drinks = pd.read_csv('http://bit.ly/drinksbycountry', index_col='country')

drinks.head(5)

drinks.iloc[2, 0]


















