# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 20:00:16 2022

@author: Mateusz
"""
helloMessage="{0:s} has {1:d} {2:s}"
print(helloMessage.format('Kate',1,'animal'))
print(helloMessage.format("Chris",100000,'$'))


line="{0:20s} costs {1:6d} €"
print(line.format("ice cream",3).upper())
print(line.format("trip to venice",119).upper())
print(line.format("pizza hawai",6).upper())

line = '{0:s} {1:d}'
 
print(line.format('ICE CREAM', 3))
print(line.format('TRIP TO VENICE', 119))
print(line.format('PIZZA HAWAII', 6))