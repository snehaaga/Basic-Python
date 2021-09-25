# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 14:15:49 2021

@author: sneha
"""
#stone-paper scissor game
a=input("First player name :")
b=input("Second player name :")
a_s = 0
b_s = 0

#noOfRounds=int(input("no of rounds: "))

for i in range(1,4):
    print("choose from stone, paper, scissor")
    c=input(a+"choose:")
    d=input(b+"choose:")
    if(c=="stone" and d=="scissor")or(c=="paper"and d=="stone")or(c=="scissor"
                                                                  and d=="paper"):
        print(a+ "win")
        a_s=a_s+1
    elif(d=="stone" and c=="scissor")or(d=="paper"and c=="stone")or(d=="scissor"
                                                                  and c=="paper"):
        print(b+ "win")
        b_s=b_s+1
    else:
        print("match draw")
print(a + "score is" ,  a_s)
print(b+ "score is" , b_s)
if(a_s>b_s):
    print(a + "win the game")
elif(b_s>a_s):
    print(b + "win the game")
else:
    print("match draw")
print("thank you for playing the game")
    
        
    

