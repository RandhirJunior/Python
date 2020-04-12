# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 18:19:02 2020

@author: Randhirs
"""

import pandas as pd

df = pd.read_csv('E:\PYTHON_ALL\Pandas\pokemon_data.csv')

##read header
print(list((df.columns)))

## read each columns

print(df[['Name', 'Type 1', 'HP']])


## read each rows
print(df.iloc[0:5])
for index, row in df.iterrows():
    print(index,row)
    print(index,row['Name'])
    
df.loc[df['Type 1'] == "Fire"]

## read a specific location (R,C)
print(df.iloc[0,1])

## it will give mean,std,min
df.describe()

## sorting of columns by alfabetic order

df.sort_values('Name',ascending=False)

## sorting multiple columns 
df.sort_values(['Type 1' , 'HP'],ascending = [1,0])

## Making changes to Dataframe



df['total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

## droping a columns from a dataframe

df = df.drop(columns=['total'])

## Adding a columns in different ways, axis=1 it add horizontaly , if axis=0 add vertically
df['Total_sum'] = df.iloc[:, 4:10].sum(axis=1)

## taken df.columns in a list and assigned it to cols
cols =list(df.columns)

## 
df =df[cols[0:4] + [cols[-1]] + cols[4:12]]

## need to save modified df to a csv file
df.to_csv('modified_data.csv',index=False)

## to save dataframe in xlsx
df.to_excel('modified_data.xlsx',index=False)

## to save as tab sepeartor
df.to_csv('modified_data.txt',index=False,sep='\t')

#-------------------Filtering Data---&= and --|=or-------------------------------
filter_df=df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] >70)]

## resetting index of filter_df ,by default it saves old indexes too, by
## using inplace=True no need to assign in new dataframe , it will save in existing dataframe
filter_df.reset_index(drop=True,inplace=True)

## or condition
filter_df1=df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]

## to drop old indexes from dataframe
filter_df1=filter_df1.reset_index(drop=True)

## if you want to filter a string in dataframe
df.loc[~df['Name'].str.contains('Mega')]

## filtering type 1 fire or grass
df.loc[df['Type 1'].str.contains('Fire|Grass',regex=True)]

## with regural expression
import re

df.loc[df['Type 1'].str.contains('fire|grass',flags=re.I,regex=True)] 

### Names start with pi
df.loc[df['Name'].str.contains('^pi[a-z]*',flags=re.I,regex=True)] 


##-----------------------------Conditional Changes-----------------------------------

df = pd.read_csv('modified_data.csv')

df.loc[df['Total_sum'] > 500, ['Generation','Legendary']] = 'TEST VALUES'

## we can modify these two columns values individually  too
df.loc[df['Total_sum'] > 500, ['Generation','Legendary']] = ['TEST VALUES1','TEST VALUES2']

##---------------------Aggreagte Statistics(Groupby)--------------------------

df = pd.read_csv('modified_data.csv')

df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)

df.groupby(['Type 1']).sum()

df.groupby(['Type 1']).count()

## to add new column with values in dataframe

df['count'] = 1

df.groupby(['Type 1','Type 2']).count()['count']

##------------------------- Working with Large amount of Data------------------

for df in pd.read_csv('modified_data.csv',chunksize=5):
    print("************CHUNK DF*************************")
    print(df)


