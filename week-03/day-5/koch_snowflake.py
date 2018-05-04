# from tkinter import *

# root = Tk()

# canvas = Canvas(root, width = '300', height = '100')

# canvas.pack()

# def kochrajzolo():
#     canvas.create_line()

# kochrajzolo()

# root.mainloop()

#import Python turtle module
#More info see https://docs.python.org/2/library/turtle.html
import turtle 

##Make turtle t draw a Koch fractal of 'order' and 'size'.
def drawKoch(t, order, size):
    if order == 0:          # The base case is just a straight line
        #Move the turtle forward by size
        #in the direction the turtle is headed.
        t.forward(size)
    else:
        drawKoch(t, order-1, size/3)   # Go 1/3 of the way and draw a Koch pattern with lower order and 1/3 size
        t.left(60) #Turn turtle left by 60 degrees.
        drawKoch(t, order-1, size/3)
        t.right(120) #Turn turtle right by 120 degrees.
        drawKoch(t, order-1, size/3)
        t.left(60) #Turn turtle left by 60 degrees.
        drawKoch(t, order-1, size/3)

##Initialize the turtle
t = turtle.Turtle()
t.speed(100) #Set the turtle's speed. 1 is slow and 10 is fast.
t.color("blue") #Set the turtle's color.
t.pensize(1) #Set the pen size
myWin = turtle.Screen() #Create the screen
t.hideturtle()

##Set values for order and size
order = 3
size = 300
 
##Initialize the pen position
t.up() #Pull the pen up - no drawing when moving.
t.backward(size/2) #move the pen backward by size/2
t.down() #Pull the pen down - drawing when moving.
 
##drawKoch(t, order, size) could only draw one side of the Koch snowflake
##So we need to use drawKoch(t, order, size) 3 times to draw a Koch snowflake
drawKoch(t, order, size)
t.right(120) #Turn turtle right by 120 degrees.
drawKoch(t, order, size)
t.right(120) #Turn turtle right by 120 degrees.
drawKoch(t, order, size)
 
##exit the drawing screen
myWin.exitonclick()