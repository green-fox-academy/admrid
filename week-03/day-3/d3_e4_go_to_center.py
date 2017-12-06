from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

def rajzolo(x, y):
    cwidth = 300
    cheight = 300
    canvas.create_line(x, y, cwidth/2, cheight/2, fill='green')

rajzolo(10, 20)
rajzolo(20, 20)
rajzolo(50, 30)

root.mainloop()