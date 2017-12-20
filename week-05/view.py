from tkinter import *
from PIL import ImageTk, Image
from model import *



class Printer():
    def __init__(self):
        self.root = Tk()

        self.canvas = Canvas(self.root, width='720', height='720')
        self.canvas.pack()

        self.canvas.focus_set()

        self.image_obj = None

        # HERO IMAGES LOADED:
        self.hero_down = ImageTk.PhotoImage(file = 'assets/hero-down.gif')
        self.hero_up = ImageTk.PhotoImage(file = 'assets/hero-up.gif')
        self.hero_left = ImageTk.PhotoImage(file = 'assets/hero-left.gif')
        self.hero_right = ImageTk.PhotoImage(file = 'assets/hero-right.gif')

        self.images = []
        self.hero_img = None

    # load the .gif image file
    # imagefile_to_draw = PhotoImage(file='assets/floor.gif')
    # imagefile_to_draw = PhotoImage(file=imagefile)
    # opened_image = Image.open(imagefile)

    def drawer(self, thing_to_draw):
        # print(issubclass(thing_to_draw, Tile))
        if isinstance(thing_to_draw, Tile):
            opened_image = Image.open(thing_to_draw.imagefile)
            image_obj = ImageTk.PhotoImage(opened_image)
            self.images.append(image_obj)
            self.canvas.create_image(thing_to_draw.x, thing_to_draw.y, anchor=NW, image=image_obj)
            self.canvas.update()
        
        elif isinstance(thing_to_draw, Hero):
            opened_image = Image.open(thing_to_draw.imagefile)
            self.image_obj = ImageTk.PhotoImage(opened_image)
            self.hero_img = self.canvas.create_image(thing_to_draw.x, thing_to_draw.y, anchor=NW, image=self.image_obj, tags='myhero')
            self.canvas.update()

    # root.mainloop()