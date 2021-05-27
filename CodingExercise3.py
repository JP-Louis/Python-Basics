# -*- coding: utf-8 -*-
"""
Created on Thu May 27 14:56:02 2021

@author: james
"""
#Coding Exercise 3

line = "--------"

print("1." + line)
print("Hello World"[8])

print("2. " + line)
ink = "Thinker"
print(ink[2:5])
s='hello'
print(s[1])

print("3. " + line)
s='Sammy'
print(s[2:])

print("4. " + line)
m = "Mississippi"
print(m[3:8])

print("5. " + line)
word = "Racecar Racecar".replace(" ", "")
word2 = word[::-1]

if (word.lower() == word2.lower()):
    print(True)
else:
    print(False)

