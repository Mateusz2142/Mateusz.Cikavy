# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 20:26:27 2022

@author: Mateusz
"""
five=5
three=3
five+three
print(type(five+three))
print(type(five/three))
import sys
print(sys.maxsize)
veryBigValue=99999999999999999999999999999999999999999999999999
print(veryBigValue+1)
print((veryBigValue+1)/2)
print(type(((veryBigValue+1)/2)))
print(five//three)
print(five % three)
print(float('inf'))
print(type(float('inf')))

name='Chris'
age=17
daysInYear=365
message="{0:s} is {1:d} years old, so is about {2:d} days old"
print(message.format (name,age,daysInYear*age))


a=1234567890
b=12345
message1="{0:d} divided by {1:d} is {2:d} and rest is {3:d}"
print(message1.format(a,b,a//b,a%b))