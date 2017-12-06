from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.

canvas.create_rectangle(10, 20, 40, 50, fill='green')
canvas.create_rectangle(40-5, 70-5, 100, 60, fill='yellow')
canvas.create_rectangle(100-5, 100-5, 200, 200, fill='blue')
canvas.create_rectangle(150-5, 150-5, 155, 155, fill='red')

root.mainloop()