from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

def rajzolo(x, y):
    cwidth = 300
    cheight = 300
    # x = 0
    # y = 0
    for i in range(0, 15):
        x += 20
        canvas.create_line(x, y, cwidth/2, cheight/2, fill='red')
    for i in range(0, 15):
        y += 20
        canvas.create_line(x, y, cwidth/2, cheight/2, fill='red')
    for i in range(0, 15):
        x -= 20
        # y = 300
        canvas.create_line(x, y, cwidth/2, cheight/2, fill='red')
    for i in range(0, 15):
        # x = 0
        y -= 20
        canvas.create_line(x, y, cwidth/2, cheight/2, fill='red')

rajzolo(0, 0)

root.mainloop()