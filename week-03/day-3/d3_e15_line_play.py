from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

# for l in range(0, 10):
#     y = 30 * l
#     if l % 2 == 0:
#         for i in range(0, 5):
#             x = 30 * i * 2
#             canvas.create_rectangle(x, y, x + wl, y + wl, fill='black') 
#             canvas.create_rectangle(x + wl, y, x + wl * 2, y + wl, fill='white') 

def rajzolo():
    x = 0
    y = 0
    for i in range(0, 15):
        x += 20  
        y += 20  
        canvas.create_line(x, 0, 300, y, fill='purple') 
    for i in range(0, 15):
        x -= 20  
        y -= 20  
        canvas.create_line(0, y, x, 300, fill='green') 

rajzolo()

root.mainloop()