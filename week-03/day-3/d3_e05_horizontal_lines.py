from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

def rajzolo(x, y):
    if x >= 250:
        canvas.create_line(x, y, x-50, y, fill='green')
    else:
        canvas.create_line(x, y, x+50, y, fill='green')

rajzolo(10, 20)
rajzolo(20, 20)
rajzolo(50, 30)

root.mainloop()