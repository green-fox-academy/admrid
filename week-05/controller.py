from model import *
from view import *

map = Map()
hero = Hero()

printer = Printer()


for i in range(len(map.map_lista)):
    printer.drawer(map.map_lista[i])

def on_key_press(e):
    # print(e)
    if e.keysym == 'Up':
        hero.move('up')
        printer.canvas.move(hero.imagefile, 0, 72)        
        # print('up')
    elif e.keysym == 'Down':
        hero.move('down')
        printer.canvas.move(hero.imagefile, 0, -72)        
        # print('down')
    elif e.keysym == 'Right':
        hero.move('right')
        printer.drawer(hero)
        # print('right')
    elif e.keysym == 'Left':
        hero.move('left')
        printer.drawer(hero)
        # print('left')


printer.canvas.bind("<KeyPress>", on_key_press)

printer.drawer(hero)


printer.root.mainloop()