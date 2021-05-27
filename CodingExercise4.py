# -*- coding: utf-8 -*-
"""
Created on Thu May 27 15:10:38 2021

@author: james
"""

line = "--------"

print("1. " + line)
li = ["One", 2, 3.01]
print(li)

print("2. " + line)
li = [1, 1, [1,2]]
print(li[2][1])

print("3. " + line)
lst = ['a','b','c']
print(lst[1:])

print("4. " + line)
dic = {'Sunday':1, 'Monday':2, 'Tuesday':3, 
       'Wednesday':4, 'Thursday':5, 'Friday':6,
       'Saturday':7}
print(dic.items())

print("5. " + line)
d={'k1':[1,2,3]}
#print(d[k1][1]) improper syntax of trying to access a dictonary, they're unordered
#d.get('k1')[1] proper accessing syntax


print("6. " + line)
li = [1,[2,3]]
tu = tuple(li)
print(type(tu))

print("7. " + line)
m = "Mississippi"
m2 = m[3:8]
print(m2)

print("8. " + line)
m2 = m2 + 'X'
print(m2)

print("9. " + line)
print(set([1,1,2,3]))

print("10. " + line)
x = range(2000, 3200)
nums = []

for y in x:
    if(y % 7 == 0 and y % 5 != 0):
        nums.append(y)       
print(nums)

print("11. " + line)
total = 1
start = 1

while (start <= 8):
    total = total * start
    start+=1

print(total)

print("12. " + line)
n = 10
dic = {}

for x in range(1, n):
    dic.update({x:(x*x)})
    
print(dic.items())


print("13. " + line)
strInput = "34,67,55,33,12,98"
lst = list(strInput.split(','))
tpl = tuple(lst)
print(lst)
print(tpl)

print("14. " + line)
def getString():
    temp = input("Input: ")
    return temp

def printString(str1):
     print(str1.upper())
    
printString(getString())

    
    