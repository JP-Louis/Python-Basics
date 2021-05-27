# -*- coding: utf-8 -*-
"""
Created on Thu May 27 16:33:41 2021

@author: james
"""
line = "--------\n"
people = ["Tommy", "Chucky", "Phil", "Lil"] 
people1 = ["Tommy", "Chucky", "Phil", "Lil"] 
people2 = ["Angelica", "Suzie"]
people3 = people + people2
people4 = []

#Three is a Crowd
def crowd_test(people):
    print(people)
    if (len(people) >= 3):
        print("The room is crowded!")
        while(len(people) >= 3):
            print("Goodbye {}!".format(people.pop()))      
    print(people)
   
#Three is a Crowd - Pt. 2
def crowd_test2(people):
    print(people)
    if (len(people) >= 3):
        print("The room is crowded!")
        while(len(people) >= 3):
            print("Goodbye {}!".format(people.pop()))
    else:
        print("The room isn't very crowded")
    print(people) 
    
#Six is a mob
def crowd_test3(people):
    print(people)
    size = len(people)
    if (size > 5):
        print("There's a mob in this room!")
    elif (size >= 3):
        print("The room is crowded!")
    elif(size == 0):
        print("The room is empty")
    else:
        print("The room isn't crowded")
    print(people)



print("1." + line)    
crowd_test(people)
print("2." + line) 
crowd_test2(people2)
print("3." + line) 
crowd_test3(people1)
