# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 20:48:47 2022

@author: Mateusz
"""
IsWeekend=True
print("is weekend =",IsWeekend)

Temperatura = 25
print("Temperatura=",Temperatura)

ToDoList=''
print("ToDoList=",ToDoList)

IsHappy=IsWeekend and Temperatura >= 20 and ToDoList == '' \
or not IsWeekend and Temperatura <20 and ToDoList !=''
print("IsHappy=",IsHappy)

isAutomaticMode=False
print("Automatic mode:",isAutomaticMode)
is80PercentLight=True
print("Is the light good:",is80PercentLight)
isDirectLight=True
print("is sun low:",isDirectLight)
isRainy=True
print("Is it rainy:",isRainy)
turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)
print("Turns lights on:",turnLightsOn)