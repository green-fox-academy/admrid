from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bd='0')
canvas.pack()

# fill the canvas with a checkerboard pattern.

x = 0
y = 0
wl = 30

for l in range(0, 10):
    y = 30 * l
    if l % 2 == 0:
        for i in range(0, 5):
            x = 30 * i * 2
            canvas.create_rectangle(x, y, x + wl, y + wl, fill='black') 
            canvas.create_rectangle(x + wl, y, x + wl * 2, y + wl, fill='white') 
    else:
        for i in range(0, 5):
            x = 30 * i * 2
            canvas.create_rectangle(x, y, x + wl, y + wl, fill='white') 
            canvas.create_rectangle(x + wl, y, x + wl * 2, y + wl, fill='black') 

root.mainloop()