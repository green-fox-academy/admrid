from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]

x = 0

for i in range(1, 21):
    x += 10
    canvas.create_rectangle(x, x, x+10, x+10, fill='purple')  

root.mainloop()