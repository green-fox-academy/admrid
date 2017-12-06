from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.

canvas.create_line(10, 10, 280, 10, fill='red')
canvas.create_line(10, 10, 10, 280, fill='yellow')
canvas.create_line(280, 10, 280, 280, fill='green')
canvas.create_line(10, 280, 280, 280, fill='blue')

root.mainloop()