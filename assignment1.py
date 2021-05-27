# -*- coding: utf-8 -*-
"""
Created on Wed May 26 22:20:24 2021
@author: james
"""

#Coding Exercise 2

line = "--------"

print("1. " + line)
grandTotal1 = 50+50
grandTotal2 = 100-10
print(grandTotal1)
print(grandTotal2)

print("2. " + line)
#num1 = 30+*6 Intended Error
#num2 = 6^6 Intended Error
num3 = 6**6
num4 = 6+6+6+6+6+6
print(num3)
print(num4)

print("3. " + line)
print("Hello World")
print("Hello World : 10")

print("4. " + line)
p = 800000 #Sum borrowed
r = .06 #Interest Rate
inc = r/12 #The monthly increase
m = 10000 #The Monthly payments towards the debt
count = 0;

while (p > 0):
    p = (p + (p * inc)) - m
    count += 1
print("Months: {}".format(count))
