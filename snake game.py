# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 16:24:20 2021

@author: sneha
"""
#vector---store multiple items in single variable
#lambda function----reduce the line of code

#snake

from random import randrange
from turtle import *
from freegames import vector,square
bgcolor("yellow")
title("snake")
food=vector(0,0)
snake=[vector(10,0)]
aim=vector(0, -10)

def change(x,y):
    aim.x=x
    aim.x=y

def inside(head):
    return -200<head.x<190 and -200<head.y<190

def move():
    head=snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x,head.y,11,'red')
        update()
        return
    snake.append(head)
    
    if head==food:
        print("your score",len(snake))
        food.x=randrange(-15,15)*10
        food.x=randrange(-15,15)*10
        
    else:
        snake.pop(0)
        
    clear()
     
    for body in snake:
        square(body.x, body.y, 11, 'block')
    square(body.x, body.y, 11, 'green')
    update()
    outliner(move,100)
     
setup(420,420,370,0)
hideturtle()
tracer(false)
listen()

onkey(lambda:change(10,0),'right')
onkey(lambda:change(-10,0),'left')
onkey(lambda:change(0,10),'up')
onkey(lambda:change(0,-10),'down')

move()
done()
