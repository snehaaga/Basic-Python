# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:44:30 2021

@author: sneha
"""
#operators

a=200
b=300
if(a<b):
    print("b is greater than a")
elif(a==b):
    print("b is equal to a")
else:
    print("b is less than a")


#to find number is positive or not
a=int(input())
if(a>0):
    print("a is a positive number")
elif(a==0):
    print("a is neither positive nor negative")
else:
    print("a is negative number")


#to find the greatest of the number
print("enter 1st number")
a=int(input())
print("enter 2nd number")
b=int(input())
print("enter 3rd number")
c=int(input())
if(a>b and a>c):
    print("a i sgreatest number")
elif(b>c):
    print("b is the greatest number")
else:
    print("c is the greatest number")
    
