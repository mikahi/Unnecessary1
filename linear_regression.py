"""
Created on Wed Jul 13 14:26:20 2016

@author: mikalimcaoco
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import statsmodels.api as sm

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

'''
print loansData['Interest.Rate'][0:5]
print loansData['Loan.Length'][0:5]
print loansData['FICO.Range'][0:5]
'''

loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: x.rstrip('%'))
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: x.rstrip('months'))

#print loansData['Interest.Rate'][0:5]
#print loansData['Loan.Length'][0:5]

'''converting data into a string and splitting it'''
loansData['FICO.Score'] = loansData['FICO.Range']


loansData['FICO.score'] = loansData['FICO.Range'].map(lambda x: x.split('-'))
loansData['FICO.score'] = loansData['FICO.Score'].map(lambda x: int(x[0]+x[1]+x[2]))

FICO=[] #declare an empty array
#loansData.columns()
for j in range(len(A)):   #for j in between 0 to len(A)
  B = A[j].split("-")     #split each sub-array on - and save it to B
  #C = int(B[0], B[1])    #convert the str to int
  #C = np.mean(C)         #finding the mean of B[0] and B[1]
  C = float(B[0])           #convert the string to int, using only the first value
  FICO.append(C)          #append each C to the empty array, using first value
loansData['FICO.Score']=FICO

plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
plt.show()

#plots on the diagonal showing histogram for each variable. 
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.show()
#why is this not shwoing  interest rate and FICO


#this part onwards i do not understand

#regression analysis of the cleaned up columns
loansData['Interest.Rate'] = loansData['Interest.Rate'].astype(float)
intrate = loansData['Interest.Rate']
intrate = [int(x) for x in intrate]
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

#the columns are returned as Series, so reshape required.
#the matrix transpose takes the column and return them as 1d-array 
y = np.matrix(intrate).transpose()  #dependent variable
print (y)
x1 = np.matrix(fico).transpose()    #independent variable
x2 = np.matrix(loanamt).transpose() #independent variable
print(x1)
print(x2)

#take the independent matrix and create an input matrix, 1 col for each variable
x = np.column_stack([x1,x2])

#creating the linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
print f.summary()

