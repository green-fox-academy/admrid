from tkinter import *

root = Tk()

canvas = Canvas(root, width='600', height='600', bg='yellow')
canvas.pack()

def rajzolo(wid, hei, rec):
    if rec > 0:
        canvas.create_line(0, hei//3, wid, hei//3)
        canvas.create_line(0, hei//3*2, wid, hei//3*2)
        canvas.create_line(wid//3, 0, wid//3, hei)
        canvas.create_line(wid//3*2, 0, wid//3*2, hei)
        return rajzolo(wid//3, hei//3, rec-1)

rajzolo(600, 600, 4)

root.mainloop()