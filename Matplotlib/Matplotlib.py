# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 00:26:07 2020

@author: Randhirs
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0,1,2,3,4]
y = [0,2,4,6,8]

## Resize your Graph
plt.figure(figsize=(5,3), dpi=100)

## Ploting the graph ,keyword Arguments Notations
#plt.plot(x,y, label='2x', color='green', linewidth=2, marker='.', markersize=12, markeredgecolor='red', linestyle='--')

# use short hand notations 
#fnt='[color],[marker],[line]'

plt.plot(x,y, 'r<--', label='2x')

## Line number 2nd
x2 = np.arange(0,4.5,0.5)

# Plot part of the graph to plot point
plt.plot(x2[:6],x2[:6]**2, 'b', label='x**2')

## Plot remaining of the graph as a dot
plt.plot(x2[5:],x2[5:]**2, 'b--')

## Title of the graph
plt.title('My First Graph',fontdict={'fontname':'Comic Sans Ms','fontsize':20})

## Plot X and Y
plt.xlabel("X-axis")
plt.ylabel("y-axis")

## X,Y axis Tickmarks (scale of your graph)
plt.xticks([0,1,2,3,4])
#plt.yticks([0,2,4,6,8,10])

## to plot the legend
plt.legend()

## To save the Graph(dpi=300 is a good for high resolutions)
plt.savefig('mygraph.png',dpi=300)

plt.show()




#---------------------BAR CHART----------------------
labels =['A','B','C']
values = [1,4,2]

bars = plt.bar(labels,values)

patterns = ['/', '^', '*']
for bar in bars:
    bar.set_hatch(patterns.pop())

"""
bars[0].set_hatch('/')
bars[1].set_hatch('o')
bars[2].set_hatch('*')
"""

plt.figure(figsize=(6,4))

plt.show()








