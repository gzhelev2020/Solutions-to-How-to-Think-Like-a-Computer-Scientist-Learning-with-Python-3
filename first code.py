#Solutions to How to Think Like a Computer Scientist with Python 3
#by Georg Z

#Import Packages
import math
import turtle

#Basic mathematical functions in Python

# y=3**2
# x=2
# print(y+x)
# 
# print("Hellow world!")
# 
# print(type(['a', 2]))
# 
# l=[10,2.2,"Hello",[0,2]]

# Design a Clock


#total_secs = int(input("How many seconds, in total?"))
# total_secs = 9010
# hours = total_secs // 3600
# print(hours)
# secs_still_remaining = total_secs % 3600
# print(secs_still_remaining)
# minutes = secs_still_remaining // 60
# print(minutes)
# secs_finally_remaining = secs_still_remaining % 60
# 
# print("Hrs=", hours, " mins=", minutes, "secs=", secs_finally_remaining)


#Attempt at converting integer to time (unsuccessfull)
# import pandas as pd
# 
# t=419
# a = pd.to_datetime(t, format='%H%M')
# print(a.hour)
# print(a.minute)

#Exercises Ch. 2

# a="All"
# b="work"
# c="and"
# d="no"
# e="play"
# f="makes"
# g="Jack"
# h="a"
# i="dull"
# j="boy"
# 
# print(a,b,c,d,e,f,g,h,i,j)

#basic math 2+2

# print(5 % 2)
# print(6 % 6)
# print(15 % 12)
# print(12 % 15)

# Introduction to Turtles

# import turtle
# wn = turtle.Screen()
# alex = turtle.Turtle()
# alex.pensize(25)
# alex.shape("turtle")
# alex.turtlesize(10)
# 
# import random
# alex.heading()
# alex.left(random.randint(1000,2000))
# alex.forward(200)
# 
# wn.mainloop()

#Draw non-repeating thinkgs with a turtle without a loop

# import turtle
# color = input("Which color should be background be?")
# wn = turtle.Screen()
# wn.bgcolor(str(color))
# wn.title("Hello, Georg!")
# 
# tess = turtle.Turtle()
# tess.color = ("white")
# tess.pensize(50)
# 
# alex = turtle.Turtle()
# 
# alex.forward(500)
# alex.left(90)
# alex.forward(500)
# 
# tess.forward(50)
# tess.left(36)
# tess.forward(100)
# tess.right(120)
# tess.forward(15)
# tess.forward(50)
# tess.left(36)
# tess.forward(100)
# tess.right(120)
# tess.forward(15)
# tess.forward(50)
# tess.left(36)
# tess.forward(100)
# tess.right(120)
# tess.forward(15)
# tess.forward(50)
# tess.left(36)
# tess.forward(100)
# tess.right(120)
# tess.forward(15)
# tess.forward(50)
# tess.left(36)
# tess.forward(100)
# tess.right(120)
# tess.forward(15)
# tess.forward(50)
# tess.left(36)
# tess.forward(100)
# tess.right(120)
# tess.forward(15)
# tess.forward(50)
# tess.left(36)
# tess.forward(100)
# tess.right(120)
# tess.forward(15)
# 
# wn.mainloop()

#Write a Birthday Invitation using a for Loop


# for f in ["Joe","Zoe","Brad","Angelina","Zuki","Thandi","Paris"]:
#     invite = "Hi " + f + ". Please come to my party on Saturday!"
#     print(invite)
# # more code can follow here ...

#Drunk Pirate

# import turtle
# import random
# 
# wn = turtle.Screen()
# tess = turtle.Turtle()
# tess.shape("turtle")
# tess.speed(0)
# 
# coin = random.randint(0,1)
# xs = [160, -43, 270, -97, -43, 200, -940, 17, -86]
# 
# tess.setheading(0)
# print(tess.heading())
# for c in range(len(xs)):
#     if coin == 0:
#         tess.forward(100)
#         tess.left(xs[c])
# 
#     else: 
#          tess.forward(100)
#          tess.left(xs[c])
# print(tess.heading())

#Triangle

# tess = turtle.Turtle() # Create tess and set some attributes
# tess.color("hotpink")
# tess.pensize(5)
# for i in range(18):
#     tess.forward(80) # Make tess draw equilateral triangle
#     tess.left(20)

# Ch. 2 Ex. 10.

# import turtle
# wn = turtle.Screen()
# tess = turtle.Turtle()
# 
# for i in range(5):
#     tess.forward(500)
#     tess.right(216)
#     
# tess.forward(500)
# 
# print(216*5)


# Ex. 11

# import turtle
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()
# tess.shape("turtle")
# tess.color("blue")
# 
# tess.turtlesize(1.5)
# tess.penup()
# tess.stamp()
# tess.pensize(5)
# 
# 
# for i in range(12):
#     tess.forward(120)
#     tess.pendown()
#     tess.forward(10)
#     tess.penup()
#     tess.forward(20)
#     tess.stamp()
#     tess.right(180) 
#     tess.forward(150)
#     for j in range(1):
#         tess.right(150)
#         
# tess.setheading(0)
# wn.mainloop()

# Ex. 12

# import turtle
# tess = turtle.Turtle()
# print(type(tess))
# #the type is a class

#Range is better than listing things manually


# for x in range(10):
#     print(x)


#Programm two turtles to draw Something

# import turtle
# wn = turtle.Screen() # Set up the window and its attributes
# wn.bgcolor("lightgreen")
# wn.title("Tess & Alex")
# 
# tess = turtle.Turtle() # Create tess and set some attributes
# tess.color("hotpink")
# tess.pensize(5)
# 
# alex = turtle.Turtle() # Create alex
# 
# tess.forward(80) # Make tess draw equilateral triangle
# tess.left(120)
# tess.forward(80)
# tess.left(120)
# tess.forward(80)
# tess.left(120) # Complete the triangle
# 
# tess.right(180) # Turn tess around
# tess.forward(80) # Move her away from the origin
# 
# alex.forward(50) # Make alex draw a square
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# 
# wn.mainloop()

#Introduce a Loop


# import turtle
# wn = turtle.Screen()
# 
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()
# tess.shape("turtle")
# tess.color("blue")
# 
# tess.penup() # This is new
# size = 20
# for i in range(30):
#     tess.stamp() # Leave an impression on the canvas
#     size = size + 2**2 # Increase the size on every iteration
#     tess.forward(size) # Move tess along
#     tess.right(10) # ... and turn her
# 
# tess.color("red")
# 
# wn.mainloop()


# Ch. 4 Functions

## Assign Function

# import turtle
# 
# def draw_square(t, sz):
#     for i in range(4):
#         t.forward(sz)
#         t.left(90)
#         
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# wn.title("Alex meets a function")
# 
# alex = turtle.Turtle()
# draw_square(alex, 150)
# wn.mainloop()

#Debug an assigned Function with a loop

# import turtle
# __import__("turtle").__traceable__ = False
# 
# def draw_multicolor_square(t, sz):
#     """Make turtle t draw a multi-color square of sz."""
#     for i in ["red", "purple", "hotpink", "blue"]:
#         t.color(i)
#         t.forward(sz)
#         t.left(90)
# 
# wn = turtle.Screen() # Set up the window and its attributes
# wn.bgcolor("lightgreen")
# 
# tess = turtle.Turtle() # Create tess and set some attributes
# tess.pensize(3)
# 
# size = 20 # Size of the smallest square
# for i in range(15):
#     draw_multicolor_square(tess, size)
#     size = size + 10 # Increase the size for next time
#     #tess.forward(10) # Move tess along a little
#     #tess.right(18) # and give her some turn
# 
# wn.mainloop()

#Compound Interest with a fruitfull function

# def final_amt(p, r, n, t):
# 
#     """
#     Apply the compound interest formula to p
#     to produce the final amount.
#     """
# 
#     a = p * (1 + r/n) ** (n*t)
#     return a # This is new, and makes the function fruitful.
# 
# # now that we have the function above, let us call it.
# toInvest = float(input("How much do you want to invest?"))
# fnl = final_amt(toInvest, 0.08, 12, 5)
# print("At the end of the period you’ll have", fnl)

#Refactoring the Code

# import turtle
# #__import__("turtle").__traceable__ = False
# 
# def make_window(colr, ttle):
#     """
#     Set up the window with the given background color and title.
#     Returns the new window.
#     """
#     w = turtle.Screen()
#     w.bgcolor(colr)
#     w.title(ttle)
#     return w
# 
# 
# def make_turtle(colr, sz):
#     """
#     Set up a turtle with the given color and pensize.
#     Returns the new turtle.
#     """
#     t = turtle.Turtle()
#     t.color(colr)
#     t.pensize(sz)
#     return t
# 
# 
# wn = make_window("lightgreen", "Tess and Alex dancing")
# tess = make_turtle("hotpink", 5)
# alex = make_turtle("black", 1)
# dave = make_turtle("yellow", 2)


# Ch. 4 Exercises

# Ex. 1

# def make_square(t, dist, angle):
#     """ Define Turtle draws square function """
#     for i in range(4):
#         t.forward(dist)
#         t.left(angle)
#     t.penup()
#     t.forward(dist+20)
#     t.pendown()
# 
# import turtle
# 
# def make_window(colr, ttle):
#     """
#     Set up the window with the given background color and title.
#     Returns the new window.
#     """
#     w = turtle.Screen()
#     w.bgcolor(colr)
#     w.title(ttle)
#     return w
#     
# def make_turtle(colr, sz):
#     t = turtle.Turtle()
#     t.color(colr)
#     t.pensize(sz)
#     return t
# 
# wn = make_window("lightgreen", "Tess and Alex dancing")
# tess = make_turtle("hotpink", 5)
# for m in range(5):
#     make_square(tess, 20, 90)

# Ex. 2

# def make_square(t, dist):
#     """ Define Turtle draws square function """
#     for i in range(4):
#         t.forward(dist)
#         t.left(90)
# 
# import turtle
# 
# def make_window(colr, ttle):
#     """
#     Set up the window with the given background color and title.
#     Returns the new window.
#     """
#     w = turtle.Screen()
#     w.bgcolor(colr)
#     w.title(ttle)
#     return w
#     
# def make_turtle(colr, sz):
#     t = turtle.Turtle()
#     t.color(colr)
#     t.pensize(sz)
#     return t
# 
# wn = make_window("lightgreen", "Tess and Alex dancing")
# tess = make_turtle("hotpink", 5)
# dist = 20
# for m in range(5):
#     make_square(tess, dist)
#     dist = dist + 20
#     tess.penup()
#     tess.goto(tess.xcor()-10, tess.ycor()-10)
#     tess.pendown()
# 
# wn.mainloop()

#Ex. 3

# def draw_poly(t, n, sz):
#     """ Define Turtle draws poly function """
#     for i in range(8):
#         t.forward(50)
#         t.left(45)
# 
# import turtle
# 
# def make_window(colr, ttle):
#     """
#     Set up the window with the given background color and title.
#     Returns the new window.
#     """
#     w = turtle.Screen()
#     w.bgcolor(colr)
#     w.title(ttle)
#     return w
#     
# def make_turtle(colr, sz):
#     t = turtle.Turtle()
#     t.color(colr)
#     t.pensize(sz)
#     return t
# 
# wn = make_window("lightgreen", "Tess and Alex dancing")
# tess = make_turtle("hotpink", 5)
# 
# for m in range(5):
#     draw_poly(tess, 8, 50)
# 
# wn.mainloop()

#Ex. 4

# def make_square(t, dist):
#     """ Define Turtle draws square function """
#     for i in range(4):
#         t.forward(dist)
#         t.left(90)
# 
# import turtle
# 
# def make_window(colr, ttle):
#     """
#     Set up the window with the given background color and title.
#     Returns the new window.
#     """
#     w = turtle.Screen()
#     w.bgcolor(colr)
#     w.title(ttle)
#     return w
#     
# def make_turtle(colr, sz):
#     t = turtle.Turtle()
#     t.color(colr)
#     t.pensize(sz)
#     return t
# 
# wn = make_window("lightgreen", "Tess and Alex dancing")
# tess = make_turtle("hotpink", 5)
# dist = 50
# dir = 45
# for m in range(5):
#     make_square(tess, dist)
#     tess.penup()
#     tess.goto(tess.xcor()+10, tess.ycor()-10)
#     tess.pendown()
#     tess.setheading(dir+10)
# 
# wn.mainloop()

#Ex. 4 Solution

# import turtle
# 
# def draw_square(turtle, size):
#     for i in range(4):
#         turtle.forward(size)
#         turtle.left(90)
# 
# if __name__ == "__main__":
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#     alex = turtle.Turtle()
#     alex.color("blue")
#     alex.pensize(3)
#     boxes = 20
# 
#     for _ in range(boxes):
#         draw_square(alex, 50)
#         alex.right(360 / boxes)
# 
#     wn.mainloop()
    
# Ex. 5

# import turtle
# 
# def draw_square(turtle, size):
#     for i in range(1):
#         turtle.right(90)
#         turtle.forward(size)
# 
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# alex = turtle.Turtle()
# alex.color("blue")
# alex.pensize(4)
# boxes = 71
# size = 10
# 
# for _ in range(boxes):
#     size= size + 5
#     draw_square(alex, size)
#     alex.left(360 / 200)
# 
# 
# wn.mainloop()

#Ex. 6

# def draw_poly(t, n, sz):
#     """ Define Turtle draws poly function """
#     for i in range(n):
#         t.forward(50)
#         t.left(sz)
#         
# def draw_equitriangle(t, sz):
#     draw_poly(t, 3, sz)
#     
# import turtle
# 
# def make_window(colr, ttle):
#     """
#     Set up the window with the given background color and title.
#     Returns the new window.
#     """
#     w = turtle.Screen()
#     w.bgcolor(colr)
#     w.title(ttle)
#     return w
#     
# def make_turtle(colr, sz):
#     t = turtle.Turtle()
#     t.color(colr)
#     t.pensize(sz)
#     return t
# 
# wn = make_window("lightgreen", "Tess and Alex dancing")
# tess = make_turtle("hotpink", 5)
# 
# draw_equitriangle(tess, 120)
#     
# wn.mainloop()

# Ex. 7

# def sum_to(n):
#     result = print(sum(list(range(n+1))))
# 
# sum_to(10)

#Ex. 8 Area of a Circle

# def area_of_circle(r):
#     result = math.pi*r**2
#     print(result)
# 
# area_of_circle(10)

#Ex. 9

# import turtle
# 
# def draw_star(t, l, a):
#     for i in range(5):
#         t.right(a)
#         t.forward(l)
# 
# def make_turtle(colr, sz):
#     t = turtle.Turtle()
#     t.color(colr)
#     t.pensize(sz)
#     return t
# 
# def make_window(colr, ttle):
#     """
#     Set up the window with the given background color and title.
#     Returns the new window.
#     """
#     w = turtle.Screen()
#     w.bgcolor(colr)
#     w.title(ttle)
#     return w
# 
# wn = make_window("lightgreen", "Tess and Alex dancing")
# tess = make_turtle("hotpink", 5)
# 
# for m in range(5):
#     draw_star(tess, 100, 144)
#     tess.penup()
#     tess.right(144)
#     tess.forward(350)
#     tess.pendown()
# wn.mainloop()











# Ch. 5: Conditionals
#Boolean Operators (and, or, not)

# x=2
# y=3
# 
# x and False == False
# False and x == False
# y and x == x and y
# x and True == x
# True and x == x
# x and x == x

#Conditional Execution (If else)

# x=4
# if x % 2 == 0:
#     print(x, " is even.")
#     #print("Did you know that 2 is the only even number that is prime?")
# else:
#     print(x, " is odd.")
#     #print("Did you know that multiplying two odd numbers " + "always gives an odd result?")

#Pass as a Placeholder

# x=4
# if x % 2 == 0:
#     pass
# else:
#     pass

# Ommting the Else clause

# x = -6
# if x < 0:
#     print("The negative number ", x, " is not valid here.")
#     x=42
#     print("I’ve decided to use the number 42 instead.")
# 
# print("The square root of ", x, "is", math.sqrt(x))

#Chained Conditional

# def function_one():
#     print(2+2)
# def function_two():
#     print(3+3)
# def function_three():
#     print(3*3)
# 
# choice="c"
# if choice == "a":
#     function_one()
# elif choice == "b":
#     function_two()
# elif choice == "c":
#     function_three()
# else:
#     print("Invalid choice.")
    
#Nested Conditionals (to be avoided)

# x=6
# if 0 < x: # Assume x is an int here
#     if x < 10:
#         print("x is a positive single digit.")

#Return Statement
 
# def print_square_root(x):
#     if x <= 0:
#         print("Positive numbers only, please.")
#         return
#     
#     result = x**0.5
#     print("The square root of", x, "is", result)
#     
# print_square_root(9) #could also have a user generated input here using "input" and "int"

#A Turtle Bar Chart

# def draw_bar(t, height):
#     """ Get turtle t to draw one bar, of height. """
#     t.begin_fill() # Added this line
#     t.left(90)
#     t.forward(height)
#     t.write(" "+ str(height))
# 
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill() # Added this line
#     t.penup()
#     t.forward(10)
#     t.pendown()
# 
# wn = turtle.Screen() # Set up the window and its attributes
# wn.bgcolor("lightgreen")
# 
# tess = turtle.Turtle() # Create tess and set some attributes
# tess.color("blue", "red")
# tess.pensize(3)
# 
# xs = [48,117,200,240,160,260,220]
# 
# for a in xs:
#     draw_bar(tess, a)
# 
# wn.mainloop()

#Floating Point Probleme

# a = math.sqrt(2.0)
# print(a, a*a)
# print(a*a == 2.0)










#Ch. 5 Exercises

#Ex. 1

# n=list(range(0,7))
# d=("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
# #print(d[1])
# 
# def which_day(n):
#     if n == 0:
#         print(d[0])
#     elif n == 1:
#         print(d[1])
#     elif n == 2:
#         print(d[2])
#     elif n == 3:
#         print(d[3])
#     elif n == 4:
#         print(d[4])
#     elif n == 5:
#         print(d[5])
#     else:
#         print(d[6])
# 
# which_day(0)

#Ex. 1 Better Solution

# def dayw(n):
#     d=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     return print(d[n])
# 
# #dayw(2)
#     
# #Ex.2
# 
# a= 3
# b= 137
# c= dayw((a+b%7)%7)
# print(c)

#Ex. 3
#in paper

#Ex. 4 skipped

#Ex. 5 skipped

#Ex. 6

# xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
# 
# def grade(g):
#     for f in xs:
#         if f >= 75:
#             print("First")
#         elif 70 <= f < 75:
#             print("Upper Second")
#         elif 60 <= f < 70:
#             print("Second")
#         elif 50 <= f < 60:
#             print("Third")
#         elif 45 <= f < 50:
#             print("F1 Supp")
#         elif 40 <= f < 45:
#             print("F2")
#         else:
#             print("F3")
# 
# 
# grade(xs)
# print(xs)

#Ex. 7
#done

#Ex. 8 and 9

# def draw_bar(t, height):
#         t.begin_fill()  #Added this line
#         t.left(90)
#         t.forward(height)
#         if height >= 0:
#             t.write(" "+ str(height))
#         if height < 0:
#             t.penup()
#             t.forward(-35)
#             t.write(str(height))
#             t.forward(35)
#             t.pendown()
#         t.right(90)
#         t.forward(40)
#         t.right(90)
#         t.forward(height)
#         t.left(90)
#         t.end_fill()  #Added this line
#         t.penup()
#         t.forward(10)
#         t.pendown()
#       
# wn = turtle.Screen()  #Set up the window and its attributes
# wn.bgcolor("lightgreen")
#  
# tess = turtle.Turtle()  #Create tess and set some attributes
# #tess.color("blue", "white")
# tess.pensize(3)
#  
# xs = [48,-117,200,240,160,260,220]
#  
# for a in xs:
#     if a >= 200:
#         tess.color("blue", "red")
#         draw_bar(tess, a)
#     elif 100 <= a < 200:
#         tess.color("blue", "yellow")
#         draw_bar(tess, a)
#     elif a < 100:
#         tess.color("blue", "green")
#         draw_bar(tess, a)
#     elif a < 0:
#         tess.color("blue", "green")
#         draw_bar(tess, a)
# 
# 
# wn.mainloop()

#Ex. 10

# def find_hypot(a, b):
#     c_sqr = a*a + b*b
#     c = c_sqr ** 0.5
#     return print(c)
# find_hypot(2, 2)

#Ex. 11
# def is_rightangled(a, b, c):
#     if abs(a*a + b*b - c*c) < 0.000001:
#         print("Yes")
#     else:
#         print("No")
# is_rightangled(8, 15, 17)

#Ex. 12
# def is_rightangled(x1, x2, x3):
#     if x1 > x2 and x1 > x3:
#         c = x1
#         a = x2
#         b = x3
#     elif x2 > x1 and x2 > x3:
#         c = x2
#         a = x1
#         b = x3
#     else:
#         c = x3
#         a = x1
#         b = x2
#     if abs((a*a + b*b) - c*c) < 0.000001:
#         print("Yes")
#     else:
#         print("No")
# is_rightangled(4.1, 8.2, 9.168)

#Ex. 13 Floating Point Problem

#don't code as an equality
# a = math.sqrt(2.0)
# print(a, a*a)
# print(a*a == 2.0)

#instead find if value is close enough
# a = math.sqrt(2.0)
# print(a, a*a)
# print(abs(2.0-a*a) < 0.000001)












#Ch. 6 Fruitfull Functions

# def area(radius):
#     b = 3.14159 * radius**2
#     return print(b)
# 
# area(10) #must be written in the console


# Absolute Value

# def absolute_value(x):
#     if x < 0:
#         return -x
#     return x

#Word Recognition

# def find_first_2_letter_word(xs):
#     for wd in xs:
#         if len(wd) == 2:
#             return print(wd)
#     return print("")
# 
# find_first_2_letter_word(["This", "is", "a", "dead", "parrot"])
# 
# find_first_2_letter_word(["I", "like", "cheese"])

# Incremental Development
#Distance
#Functions in Functions

# def distance (x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquared = dx*dx + dy*dy
#     result = dsquared**0.5
#     print(result)
#     return result
# 
# def area(r):
#     result = math.pi*r**2
#     print(result)
#     return result
#     
# def area2(xc, yc, xp, yp):
#     radius = distance(xc, yc, xp, yp)
#     result = area(radius)
#     return print(result)
# 
# #area given points
# area2(1, 2, 4, 6)

#Boolean Functions

# def is_divisible(x, y):
#     """ Test if x is exactly divisible by y """
#     if x % y == 0:
#         return True
#     else:
#         return False
#     
# print(is_divisible(15, 5))
#     
# #Boolean Function without if Statement
#     
# def is_divisible(x, y):
#     return x % y == 0
# 
# print(is_divisible(15, 5))

#Unit Testing

# import sys
# 
# def test(did_pass): #define test
#     """ Print the result of a test. """
#     linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
#     if did_pass:
#         msg = "Test at line {0} ok.".format(linenum)
#     else:
#         msg = ("Test at line {0} FAILED.".format(linenum))
#     print(msg)
    
# def test_suite(): #define test suite
#     """ Run the suite of tests for code in this module (this file).
#     """
#     test(absolute_value(17) == 17)
#     test(absolute_value(-17) == 17)
#     test(absolute_value(0) == 0)
#     test(absolute_value(3.14) == 3.14)
#     test(absolute_value(-3.14) == 3.14)

#define functions to be tested

# def absolute_value(x): #Correct version
#     if x < 0:
#         return -x
#     return x

# def absolute_value(n): # Buggy version
#     """ Compute the absolute value of n """
#     if n < 0:
#         return 1
#     elif n > 0:
#         return n
    
#tests
    
# test_suite() # Here is the call to run the tests












#Ch. 6 Exercises
#all exercises use test function below

import sys

def test(did_pass): #define test
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
def test_suite(): #define test suite
    """ Run the suite of tests for code in this module (this file).
    """

#Ex. 1

# def turn_clockwise(i):
#     #dir = ("N", "E", "S", "W")
#     if i == "N":
#         return "E"
#     elif i == "E":
#         return "S"
#     elif i == "S":
#         return "W"
#     else:
#         return "N"
#     
# print(turn_clockwise("W"))
    
    
# def test_suite(): #define test suite
#     """ Run the suite of tests for code in this module (this file).
#     """
#     test(turn_clockwise("N") == "E")
#     test(turn_clockwise("W") == "N")
#     test(turn_clockwise(42) == None)
#     test(turn_clockwise("rubbish") == None)
#    
# test_suite()

#Ex. 2

# d=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# n= (0, 1, 2, 3, 4, 5, 6)
# 
# def day_name(i):
#     if i in n:
#         return d[i]
#     else:
#         return None
# 
# #print(day_name(2))
# def test_suite(): #define test suite
#     """ Run the suite of tests for code in this module (this file).
#     """
#     test(day_name(3) == "Wednesday")
#     test(day_name(6) == "Saturday")
#     test(day_name(42) == None)
# 
# test_suite()

#Ex. 3
# d=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# n= (0, 1, 2, 3, 4, 5, 6)
# 
# def day_num(i):
#     if i in d:
#         k = d.index(i)
#         return n[k]
#     else:
#         return None
#     
# def day_name(i):
#     if i in n:
#         return d[i]
#     else:
#         return None
# 
# def test_suite(): #define test suite
#     """ Run the suite of tests for code in this module (this file).
#     """
# test(day_num("Friday") == 5)
# test(day_num("Sunday") == 0)
# test(day_num(day_name(3)) == 3)
# test(day_name(day_num("Thursday")) == "Thursday")
# test(day_num("Halloween") == None)
# 
# test_suite()

#Ex. 4

# d=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# n= (0, 1, 2, 3, 4, 5, 6)
# 
# def day_num(i):
#     if i in d:
#         k = d.index(i)
#         return n[k]
#     else:
#         return None
#     
# def day_name(i):
#     if i in n:
#         return d[i]
#     else:
#         return None
# 
# def day_add(i, delta):
#     return day_name((day_num(i)+delta)%7) #can alose be broken down for clarity
# 
# #print(day_add("Wednesday", 19))
# 
# test(day_add("Monday", 4) == "Friday")
# test(day_add("Tuesday", 0) == "Tuesday")
# test(day_add("Tuesday", 14) == "Tuesday")
# test(day_add("Sunday", 100) == "Tuesday")
# 
# test_suite()

#Ex. 5

# d=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# n= (0, 1, 2, 3, 4, 5, 6)
# 
# def day_num(i):
#     if i in d:
#         k = d.index(i)
#         return n[k]
#     else:
#         return None
#     
# def day_name(i):
#     if i in n:
#         return d[i]
#     else:
#         return None
# 
# def day_add(i, delta):
#     return day_name((day_num(i)+delta)%7) #can alose be broken down for clarity
# 
# print(day_add("Sunday", -8))
# 
# test(day_add("Sunday", -1) == "Saturday")
# test(day_add("Sunday", -7) == "Sunday")
# test(day_add("Tuesday", -100) == "Sunday")
# 
# test_suite()

#The function already works with subtracting days.
#It works because the modulus operator allows for the exact estimation.
#See Notes for proof

#Ex. 6

# m= ("January", "February", "March", "April", "May", "June",
#     "July", "August", "September", "October", "November", "December")
# d= (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# 
# def days_in_month(i):
#     if i in m:
#         k = m.index(i)
#         return d[k]
#     else:
#         return None
#     
# print(days_in_month("February"))
# test(days_in_month("February") == 28)
# test(days_in_month("December") == 31)
# test(days_in_month("Monday") == None)

#Ex. 7

# def to_secs(h, m, s):
#     h_in_sec = h*60*60
#     m_in_sec = m*60
#     return h_in_sec + m_in_sec + s
# 
# print(to_secs(2, 30, 10))
# test(to_secs(2, 30, 10) == 9010)
# test(to_secs(2, 0, 0) == 7200)
# test(to_secs(0, 2, 0) == 120)
# test(to_secs(0, 0, 42) == 42)
# test(to_secs(0, -10, 10) == -590)
# 
# test_suite()

#Ex. 8

# def to_secs(h, m, s):
#     h_in_sec = h*60*60
#     m_in_sec = m*60
#     return math.floor(h_in_sec + m_in_sec + s)
# 
# print(to_secs(2.5, 0, 10.71))
# test(to_secs(2.5, 0, 10.71) == 9010)
# test(to_secs(2.433,0,0) == 8758)
# 
# test_suite()

#Ex. 9

# def hours_in(s):
#     return s // 3600
#     
# def minutes_in(s):
#     rem_sec = s % 3600
#     return rem_sec // 60
#     
# def seconds_in(s):
#     rem_sec = s % 3600
#     return rem_sec % 60
# 
# print(hours_in(9010))
# print(minutes_in(9010))
# print(seconds_in(9010))
# 
# test(hours_in(9010) == 2)
# test(minutes_in(9010) == 30)
# test(seconds_in(9010) == 10)
# 
# test_suite()

#Ex. 10

# test(3 % 4 == 0) #fails because there is no remainder
# test(3 % 4 == 3) 
# test(3 / 4 == 0) #division doesnt show the remainder
# test(3 // 4 == 0)
# test(3+4 * 2 == 14) #parenthesies missing
# test(4-2+2 == 0) #parenthesies missing
# test(len("hello, world!") == 13)
# 
# print(3 % 4)
# print(3 % 4)
# print(3 / 4)
# print(3 // 4)
# print(3+4 * 2)
# print(4-2+2)
# print(len("hello, world!"))

#Ex. 11

# def compare(a, b):
#     if a > b:
#         return 1
#     elif a == b:
#         return 0
#     elif a < b:
#         return -1
#     
# test(compare(5, 4) == 1)
# test(compare(7, 7) == 0)
# test(compare(2, 3) == -1)
# test(compare(42, 1) == 1)

#Ex. 12

# def hypotenuse(a, b):
#     return (a*a + b*b)**0.5
# 
# test(hypotenuse(3, 4) == 5.0)
# test(hypotenuse(12, 5) == 13.0)
# test(hypotenuse(24, 7) == 25.0)
# test(hypotenuse(9, 12) == 15.0)

#Ex. 13

# def slope(x1, y1, x2, y2):
#     return (y2-y1)/(x2-x1)
# 
# test(slope(5, 3, 4, 2) == 1.0)
# test(slope(1, 2, 3, 2) == 0.0)
# test(slope(1, 2, 3, 3) == 0.5)
# test(slope(2, 4, 1, 2) == 2.0)
# 
# def intercept(x1, y1, x2, y2):
#     return y1 - slope(x1, y1, x2, y2)*x1
# 
# test(intercept(5, 3, 4, 2) == -2.0)
# test(intercept(1, 6, 3, 12) == 3.0)
# test(intercept(6, 1, 1, 6) == 7.0)
# test(intercept(4, 6, 12, 8) == 5.0)
# test(intercept(2, 4, 1, 2) == 0)

#Ex. 14

# def is_even(n):
#     return n % 2 == 0
# 
# print(is_even(4))
# 
# test(is_even(4) == True)
# test(is_even(3) == False)

#Ex. 15

# def is_odd(i):
#     return not is_even(i)
# 
# print(is_odd(7))
# test(is_odd(7) == True)
# test(is_odd(6) == False)

#Ex. 16

# def is_factor(f, n):
#     return n % f == 0
# 
# print(is_factor(5, 12))
# test(is_factor(3, 12))
# test(not is_factor(5, 12))
# test(is_factor(7, 14))
# test(not is_factor(7, 15))
# test(is_factor(1, 15))

#Ex. 17

# def is_multiple(a, b):
#     return is_factor(b, a)
# 
# test(is_multiple(12, 3))
# test(is_multiple(12, 4))
# test(not is_multiple(12, 5))
# test(is_multiple(12, 6))
# test(not is_multiple(12, 7))

#Ex. 18

# def f2c(t):
#     return round(((t - 32) * 5) / 9)
# 
# print(f2c(36))
# test(f2c(212) == 100) # Boiling point of water
# test(f2c(32) == 0) # Freezing point of water
# test(f2c(-40) == -40) # Wow, what an interesting case!
# test(f2c(36) == 2)
# test(f2c(37) == 3)
# test(f2c(38) == 3)
# test(f2c(39) == 4)

#Ex. 19

# def c2f(t):
#     return round((t/5) * 9 + 32)
# 
# test(c2f(0) == 32)
# test(c2f(100) == 212)
# test(c2f(-40) == -40)
# test(c2f(12) == 54)
# test(c2f(18) == 64)
# test(c2f(-48) == -54)

#Ch. 7: Iteration

#Intialise a Loop

# def mysum(xs):
#     """ Sum all the numbers in the list xs, and return the total. """
#     running_total = 0 #initialise
#     for x in xs:
#         running_total = running_total + x
#     return running_total
# 
# # Add tests like these to your test suite ...
# test(mysum([1, 2, 3, 4]) == 10)
# test(mysum([1.25, 2.5, 1.75]) == 5.5)
# test(mysum([1, -2, 3]) == 2)
# test(mysum([ ]) == 0)
# test(mysum(range(11)) == 55) # 11 is not included in the list.

#While-Loop

# def sum_to(n):
#     """ Return the sum of 1+2+3 ... n """
#     ss = 0
#     v = 1
#     while v <= n:
#         ss = ss + v
#         v = v + 1
#     return ss
# 
# # For your test suite
# test(sum_to(4) == 10)
# test(sum_to(1000) == 500500)

#For-Loop

# def sum_to(n):
#     """ Return the sum of 1+2+3 ... n """
#     ss = 0
#     for v in range(n+1):
#         ss = ss + v
#     return ss
# 
# test(sum_to(4) == 10)
# test(sum_to(1000) == 500500)

#3n + 1 Sequance

def seq3np1(n):
    """ Print the 3n+1 sequence from n,
    terminating when it reaches 1.
    """
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0: # n is even
            n = n // 2
        else: # n is odd
            n = n * 3 + 1
    print(n, end=".\n")

print(seq3np1(21))

#