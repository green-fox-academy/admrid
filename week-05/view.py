from tkinter import *
from PIL import ImageTk, Image

images = []

class Printer():
    def __init__(self):
        self.root = Tk()

        self.canvas = Canvas(self.root, width='720', height='720')
        self.canvas.pack()

        self.canvas.focus_set()

    # load the .gif image file
    # imagefile_to_draw = PhotoImage(file='assets/floor.gif')
    # imagefile_to_draw = PhotoImage(file=imagefile)
    # opened_image = Image.open(imagefile)

    def drawer(self, thing_to_draw):
        opened_image = Image.open(thing_to_draw.imagefile)
        image_obj = ImageTk.PhotoImage(opened_image)
        images.append(image_obj)   
        # put gif image on canvas
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        self.canvas.create_image(thing_to_draw.x, thing_to_draw.y, anchor=NW, image=image_obj)
        self.canvas.update()

    # root.mainloop()