#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:48:58 2020

@author: anjali.kumari
"""
import turtle
s = turtle.getscreen()
t = turtle.Turtle()


t.speed(1)
t.right(90)
t.forward(100)
t.left(90)
t.backward(100)
t.goto(100,100)
t.home()
t.speed(10)

t.dot(20,"green")


turtle.bgcolor("blue")


t.fillcolor("pink")
t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)


t.end_fill()
t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
t.begin_fill()
t.circle(90)
t.end_fill()


c = t.clone()
t.color("magenta")
c.color("red")
t.circle(100)
c.circle(60)

t.goto(-200,-200)

for i in range(4):
    t.fd(100)
    t.rt(90)
    
    
    
n=10
while n <= 40:
  t.circle(n)
  n = n+10
  
  
  
u = input("Would you like me to draw a shape? Type yes or no: ")
if u == "yes":
    t.circle(150)
elif u == "no":
    print("Okay")
else:
    print("Invalid Reply")
   
    

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()



for i in range(10):
    for i in range(4):
        t.fd(100)
        t.right(90)
    t.right(36)
    
 
    
def draw_circle():
    for i in range(360):
        t.fd(1)
        t.right(1)

for i in range(6):
    draw_circle()
    t.right(6)
    

# Python program to draw  
# Spiral Square Outside In and Inside Out  
# using Turtle Programming 
import turtle   #Outside_In 
wn = turtle.Screen() 
wn.bgcolor("light green") 
wn.title("Turtle") 
skk = turtle.Turtle() 
skk.color("blue") 
  
def sqrfunc(size): 
    for i in range(4): 
        skk.fd(size) 
        skk.left(90) 
        size = size-5
  
sqrfunc(146) 
sqrfunc(126) 
sqrfunc(106) 
sqrfunc(86) 
sqrfunc(66) 
sqrfunc(46) 
sqrfunc(26) 


import turtle  #Inside_Out 
wn = turtle.Screen() 
wn.bgcolor("light green") 
skk = turtle.Turtle() 
skk.color("blue") 
  
def sqrfunc(size): 
    for i in range(4): 
        skk.fd(size) 
        skk.left(90) 
        size = size + 5
  
sqrfunc(6) 
sqrfunc(26) 
sqrfunc(46) 
sqrfunc(66) 
sqrfunc(86) 
sqrfunc(106) 
sqrfunc(126) 
sqrfunc(146) 

import turtle 
loadWindow = turtle.Screen() 
turtle.speed(2) 
  
for i in range(100): 
    turtle.circle(5*i) 
    turtle.circle(-5*i) 
    turtle.left(i) 
  
turtle.exitonclick() 


import turtle 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Pen() 
turtle.bgcolor('black') 
for x in range(360): 
    t.pencolor(colors[x%6]) 
    t.width(x/100 + 1) 
    t.forward(x) 
    t.left(59) 


import turtle
s= turtle.getscreen()
t=turtle.Turtle()
t.speed(10)
t.circle(50)




















































