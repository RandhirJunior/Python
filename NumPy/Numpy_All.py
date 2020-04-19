# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 00:34:51 2020

@author: Randhirs
"""

import numpy as np
import sys

# We can specific dtype expecitalit as dtype='int16'
array = np.array([[1,2,3],[5,6,7]] ,dtype='int32')
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])

# To get the Dimension of an array
print(array.ndim)

# To get the Shape(number of rows and columns) of an array
print(array.shape)

# Get Type
print(array.dtype)
b.dtype

# Get memory allocated for thid array 
array.itemsize
b.itemsize
# Get total size of an array ---> array size * array itemsize
array.size * array.itemsize

#Get total size of an array
array.nbytes

##---------------Accessing Changinf Specefic elements,rows,columns -------------
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a)

## Get Specific elements [row , column]
a[:,2]
a[1,-1]  ## Negative index i.e -1 from last element

## Get specific rows
a[0,:]

## Specific Columns
a[:,2]

## Geeting rows and columns by steps [star_index:End_index:stepsize]
a[0,1:6:2]

## Changing elements of an array
a[0,1] =99
a[:,4]= [20,30] # both rows 3rd columns chnage values to 20 and 30


## 3D Array-------------------------------
A_3D_Array = np.array([[[1,2] , [3,4]] , [[5,6] , [7,8]]])

print(A_3D_Array)

## Get Specific element (work outside in) A_3D_Array[0,row,column] : specify all
"""
[[[1 2]     ------>0
  [3 4]]

 [[5 6]    -------->1
  [7 8]]]

"""
A_3D_Array[0,1,1]

A_3D_Array[:,1,:]

## Replace element, element should be in same Dimension
A_3D_Array[:,1,:] = [[9,9],[8,8]]


#-----Initialization Different types of Array-----------------------------------

#1. All 0s Matrix
np.zeros(4)

np.zeros((2,3), dtype='int32')

np.zeros((2,3,4))  ##---- chunk,rows,colunns

#2. All 1's Matrix
np.ones(4)

np.ones((2,3))

np.ones((3,3,2), dtype='int32')  ## ------ chunk,rows,columns


#3. Any other number matrix full() has two arguments shape and elements
np.full((2,2),99, dtype='float32')

#4. Any other number full_like() , here creating array as a
np.full_like(a,4)


#4. Initialising a matrix with a Random decimal number
np.random.rand(4,3,2)  #---hunk,rows,colunns

#5. Random Integer number,   range ,size=(3,3)
np.random.randint(4,9,size=(3,3))

np.random.randint(-4,9,size=(3,3))

#6. Creating Identity Matrix , Square in nature
a1 = np.identity(4)
a2 = np.identity(4)

print(a1+a2)

## making Matrix as per requiremnts
sudoku = np.ones((5,5) , dtype='int32')

z = np.zeros((3,3,), dtype='int32')
z[1,1] = 9
print(z)
sudoku[1:4, 1:4] = z   # sudoku[row index range, columns index range]
print(sudoku)

## Be careful while copying Arrays!!
a = np.array([1,2,3])
b = a
b[0] = 100       
print(a)                ## here Array also got changed , bcz a and b are pointing to same loacations
print(b)

## To over come above issues use copy() like below
b = a.copy()
b[0] = 100       
print(a)            
print(b)


##---------------------------Mathematics--------------------------------------
a = np.array([1,2,3,4])
print(a)

print(a+2)
print(a*2)
print(a-2)
print(a/2)

print(a ** 2)

## Trigonametric functions  of all the values
np.sin(a)
np.cos(a)
np.tan(a)


## ------------------Linear Algebra------------------------
a = np.ones((2,3)
print(a)

b = np.full((3,2), 2)
print(b)

np.matmul(a,b)

## Finding determinant of a matrix
c = np.identity(3)
np.linalg.det(c)

## -----------------Statistics-----------------------------
stats = np.array([[1,2,3],[4,5,6]])
stats

## Axis =0 means columns by , axis =1 means row by
np.min(stats)
np.min(stats, axis=0) 

np.max(stats, axis=1)

# Add all the values of Array
np.sum(stats)

#sum by axis =1 , row by
np.sum(stats, axis=1)

#sum by axis =0 , columns by
np.sum(stats, axis=0)


#----Reorganozing Arrays---------------------
before = np.array([[1,2,3,4],[5,6,7,8,]])
print(before)

after = before.reshape((4,2))
print(after)


# ------------------Vertically stacking vectors/Matrix
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

np.vstack([v1,v2,v2,v2])


# -------------Horizontal stack---------------
h1 = np.ones((2,4))
h2 = np.zeros((2,2))

np.hstack((h1,h2))

#----------Miscellaneouse-----------------------------------

#Load data from file
filedata = np.genfromtxt('data.txt', delimiter=',')
print(filedata)

filedata = filedata.astype('int32')


# Boolean Masking and Advanced Indexing-------------
filedata > 50  

filedata[filedata > 50]

np.any(filedata > 50, axis = 0)

np.all(filedata > 50, axis = 1)            # axis =1 means rows and axis =0 means columns

((filedata > 50) & (filedata <100))

(~(filedata > 50) & (filedata <100))

# You can index with a list in numpy
a = np.array([1,2,3,4,5,6,7,8,9])
a[[1,2,-1]]







