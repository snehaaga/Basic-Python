# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:44:30 2021

@author: sneha
"""
# simple calculator


print("please enter 1st number")
a=int(input())
print("please enter 2nd number")
b=int(input())
print("enter 1 for addition")
print("enter 2 for subraction")
print("enter 3 for multiplication")
print("enter 4 for division")
n=int(input())
if(n==1):
    c=a+b
    print("the addition of" , a , "and" , b , "is" , c)
elif(n==2):
    c=a-b
    print(c)
elif(n==3):
    c=a*b
    print(c)
elif(n==4):
    c=a/b
    print(c)
else:
    print("no match")
