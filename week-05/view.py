from tkinter import *
from PIL import ImageTk, Image

class Printer():
    def __init__(self):
        self.root = Tk()

        self.canvas = Canvas(self.root, width='720', height='720')
        self.canvas.pack()

    # ToDo: ide berakni ezt: PhotoImage(file='assets/floor.gif' és a másikat mint variable, és azokat aztán a drawerbe beadni

    # load the .gif image file
    # imagefile_to_draw = PhotoImage(file='assets/floor.gif')
    # imagefile_to_draw = PhotoImage(file=imagefile)
    # opened_image = Image.open(imagefile)
        self.image_obj = 'overwrite'

    def drawer(self, thing_to_draw):
        opened_image = Image.open(thing_to_draw.imagefile)
        self.image_obj = ImageTk.PhotoImage(opened_image)   
        # put gif image on canvas
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        self.canvas.create_image(thing_to_draw.x, thing_to_draw.y, anchor=NW, image=self.image_obj)
        self.canvas.update()

    # drawer(tile)
    # root.mainloop()