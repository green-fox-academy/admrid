from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/envelope-star/r2.png]

def rajzolo():
    x = 0
    y = 150
    # for i in range(0, 15):
    #     x += 10  
    #     y += 10  
    #     canvas.create_line(x, 0, 300, y, fill='purple') 
    for i in range(0, 15):
        x += 10  
        y -= 10  
        canvas.create_line(x, 150, 150, y, fill='green')

    x = 0
    y = 150
    for i in range(0, 15):
        x += 10  
        y += 10  
        canvas.create_line(x, 150, 150, y, fill='green') 

    x = 300
    y = 150
    for i in range(0, 15):
        x -= 10  
        y += 10  
        canvas.create_line(150, y, x, 150, fill='green')

    x = 300
    y = 150
    for i in range(0, 15):
        x -= 10  
        y -= 10  
        canvas.create_line(150, y, x, 150, fill='green')

rajzolo()

root.mainloop()