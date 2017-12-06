from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.
color= '#BADC'
xx = 300

def rajzolo(x, colors):
    x = xx
    for i in range(1, 10):
        x -= 20
        color = '#' + str(i) + 'A' + str(i) + 'C' + str(i-1) + 'T'
        print(color)
        canvas.create_rectangle(150-(x/2), 150-(x/2), 150+(x/2), 150+(x/2), fill=color)    

rajzolo(xx, color)

root.mainloop() 