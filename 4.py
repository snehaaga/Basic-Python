# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 12:32:09 2021

@author: sneha
"""

#list represent []
list1 = [1,2,3,4]
list2 = [1,2,3,4,4] #list prints duplicate values
print(type(list1))
print(list1)
print(list2)
print(len(list1)) #length of list 

#muttable: we can make changes and immuttabl: we cannot make changes

#append--add element at the end of the list

list1.append(5)
print(list1)

list1.pop()
print("this is pop",list1)
list1.pop(2) #index number
print("this is pop with indexing",list1)

list1.remove(1) #element number
print(list1)

list=[1,2,3]
print(list[1]*list[-1])  #index number

#tuple
a=(1,2,3,4)
b=(1,2,3,3) #tuple allow duplicate values
print(type(a))
print(b)

#set
set={1,2,3,4,5,"sneha"} #these are unordered
print(set)
print(type(set))
set.add(6)
print(set)
set.remove(2) #element number
print(set)

#dictionary
dict={}
#key and value
dict[1]="one"
dict[2]="two"
dict[3]="two" #we can repeat value but not key
print(dict)
del dict[2]
print(dict)


