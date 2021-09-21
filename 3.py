# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:33:38 2021

@author: sneha
"""

#typecasting
a=1
print(type(a))
b=str(a)
print(type(b))
print(b)


#string----we can use '',"" or ''' ''' for string
name1 = 'vishal'
name2 = "sneha"
name3 = '''sumit'''
print("first name is",name1)
print("first name is",name2)
print("first name is",name3)

#indexing
name1="sneha"
print(name1)
print("the 1st char of",name1,"is",name1[0])
print("the last char of",name1,"is",name1[-1])
name1="neha" #update in name1
print(name1)
del name1 #del----deletes full string
#slicing
name2="priya"
print(name2[1:])


#escape charactar
a="it's sneha here"
print(a)
b='it\'s sneha here'
print(b)
c=r'it\'s sneha here'
print(c)

