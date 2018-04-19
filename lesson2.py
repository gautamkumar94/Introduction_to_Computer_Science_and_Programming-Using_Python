#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:53:01 2018

@author: gautam
"""

x = 5
if (x != 5):
    print("i am here")
else:
    print("i am here")
    
    
y=0
while(y<5):
    print(y)
    y=y+1
    
    
    
mySum = 0
for i in range(7,16,2):
    mySum += i
    print(str(mySum)+ " is the sum")
    
    
    
varA=5
varB=6

if(type(varA)==str or (type(varB)==str)):
    print("string involved")
elif(varA > varB):
    print("bigger")
elif(varA == varB):
    print("equal")
elif(varA <varB):
    print("smaller")
    
    
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))

print("****************************************")


num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num)) 