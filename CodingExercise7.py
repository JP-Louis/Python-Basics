# -*- coding: utf-8 -*-
"""
Created on Fri May 28 10:19:01 2021

@author: james
"""

line = "--------"

print("1. " + line)
nums = []
for y in range(1500, 2700):
    if(y % 7 == 0 and y % 5 == 0):
        nums.append(y)       
print(nums)

print("2. " + line)

def toCelsius(temp):
    cel = (temp - 32) * 5/9
    cel = round(cel)
    return cel
    
def toFahrenheit(temp):
    fah = (temp / (5/9)) + 32
    fah = round(fah)
    return fah

print(toCelsius(140))
print(toFahrenheit(7))


print("3. " + line)
import random
target = random.randint(0,9)
print(target)

print("4. " + line)
guess = -1
while(guess != target):
    guess = input("Please input a guess: ")
    guess = int(guess)

print("Well Guessed!")

print("5. " + line)
i = 2
for x in range(1, 10):
    if(x <= 5):
        stars = "*"*x
        print(stars)
    else:
        stars = "*" * (x-i)
        print(stars)
        i+=2

        
print("6. " + line)
def reverseString(word):
    newWord = word[::-1]
    return newWord

word = input("Please enter a word to reverse: ")
print(reverseString(word))


print("7. " + line)
series = (1, 2, 3, 4, 5, 6, 7, 8, 9)
evens = 0
odds = 0

for x in series:
    if(x % 2 == 0):
        evens+=1
    else:
        odds+=1

print("Number of even numbers: {}".format(evens))
print("Number of odds numbers: {}".format(odds))


print("8. " + line)
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for x in datalist:
    print(type(x))

print("9. " + line)
for x in range(0, 6):
    if (x == 3 or x == 6):
        continue
    print(x)

