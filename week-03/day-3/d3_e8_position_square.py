from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

def rajzolo(x, y):
    if x >= 250:
        canvas.create_rectangle(x, y, x-50, y-50, fill='green')
    else:
        canvas.create_rectangle(x, y, x+50, y+50, fill='green')

rajzolo(10, 20)
rajzolo(40, 40)
rajzolo(210, 210)

root.mainloop()