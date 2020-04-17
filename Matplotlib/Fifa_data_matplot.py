# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 23:35:58 2020

@author: Randhirs
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

## Reading fifa data
fifa = pd.read_csv('Fifa_data.csv')

##-------------------------------------Histograms--------------------------------------------

## Title of graph
plt.title('Distribuation of Players Skill in FIFA')

bins = [40,50,60,70,80,90,100]
##Ploting Histograms
plt.hist(fifa.Overall, bins=bins, color='#42c5f5')

## Labels of X and Y axis
plt.ylabel('Number of Players')
plt.xlabel('Skills level')


plt.xticks(bins)

## Saving Graph
plt.savefig('Distribuation_Player_Fifa.png',dpi=300)

plt.show()

#---------------------------------PIE CHART No 1------------------------------------------------------

## Reading the data for how many Player play with left foot
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]

## Title of graph
plt.title('Left and Right Footer Players in FIFA')

labels = ['Left','Right']
colors = ['#34cfeb','#eb34ab']

## Ploting Pie chart
plt.pie([left, right], labels=labels, colors=colors, autopct='%.2f%%')

## Saving Graph
plt.savefig('Left_Right_Footer_Players_Fifa.png',dpi=300)

plt.show()


#---------------------------------PIE CHART No 2------------------------------------------------------
## Since Weight have number and string i.e. lbs ,So we need to trim lbs from it .
##
##
fifa.Weight = [int(x.strip('lbs')) if type(x)== str else x for x in fifa.Weight]
## Changing color of graph 
plt.style.use('ggplot')
fifa.Weight[0]

## Title of graph
plt.title('Weight Distribuation of FIFA Players in (lsb)')

light = fifa.loc[fifa.Weight < 120].count()[0]
light_medium = fifa.loc[(fifa.Weight >=125) & (fifa.Weight <150)].count()[0]
medium = fifa.loc[(fifa.Weight >=150) & (fifa.Weight <175)].count()[0]
medium_heavy = fifa.loc[(fifa.Weight >=175) & (fifa.Weight <200)].count()[0]
heavy = fifa.loc[(fifa.Weight >=200)].count()[0]

##
weights = [light,light_medium,medium,medium_heavy,heavy]
labels = ['Under 125', '125-150', '150-175', '175-200', 'Over 200']
explode = (.4,.2,0,0,.4)

## Ploting Pie chart
plt.pie(weights, labels= labels, autopct='%.2f%%', pctdistance= 0.8, explode=explode)

## Saving Graph
plt.savefig('Weight_Of_Players_Fifa.png',dpi=300)
plt.show()


#---------------------------------COMPARISING PLAYER BY CLUBS------------------------------------------------------
plt.style.use('default')
plt.figure(figsize=(5,8))

barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']

madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
labels = ['FC Barcelona', 'Real Madrid']

## Title of graph
plt.title('Professional Soccer Team Comparision')

boxes = plt.boxplot([barcelona,madrid], labels= labels, patch_artist=True)

for box in boxes['boxes']:
    ## Set edge color
    box.set(color='red', linewidth=2)
    
    # Change Fill Color
    box.set(facecolor='Green')

plt.ylabel('FIFA Overall Rating')
plt.xlabel('Team')

plt.show()









