from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

x = 5

for i in range(1, 6):
    x *= 2
    canvas.create_rectangle(x, x, x+x, x+x, fill='purple')  

root.mainloop()