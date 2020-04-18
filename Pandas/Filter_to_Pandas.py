# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:24:15 2020

@author: Randhirs
"""

##--How do I apply multiple filter criteria to a pandas DataFrame?

import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('https://bit.ly/imdbratings')

movies = movies[(movies.duration >=200) & (movies.star_rating >= 8)]

## it will return True 
(movies.duration >=200) & (movies.star_rating >= 8)

## To apply multiple of filetr condition in different ways by using isin() method of dataframe
movies = movies[(movies.genre =='Crime') | (movies.genre == 'Drama') | (movies.genre == 'Action')]
movies[movies.genre.isin(['Crime', 'Drama', 'Action'])]



#-----------------------When should I use a "groupby" in pandas?------------------------

drinks = pd.read_csv('http://bit.ly/drinksbycountry')

## Tocalculate mean
drinks.beer_servings.mean()

## Continent by mean of beer_servings
mean_by_continent = drinks.groupby('continent').beer_servings.mean()

## agg() function 
mean_by_continent = drinks.groupby('continent').beer_servings.agg(['count', 'max', 'min', 'mean'])

## To calculate mean of all numeric columns 
drinks.groupby('continent').mean()

## To plot graph of means
drinks.groupby('continent').mean().plot(kind='bar')
plt.title('Beer mean by Continent')

plt.show()
