from model import *
from view import *
# import gc

# gc.disable()

map = Map()
hero = Hero()

printer = Printer()


for i in range(len(map.map_lista)):
    printer.drawer(map.map_lista[i])

def on_key_press(e):
    # print(e)
    hero_old_y = hero.y
    hero_old_x = hero.x

    if e.keysym == 'Up':    
        hero.move('up')        
        # printer.drawer(hero)
        printer.canvas.itemconfig(printer.hero_img, image = printer.hero_up)
        printer.canvas.move(printer.hero_img, hero.x - hero_old_x, hero.y - hero_old_y)
        # printer.canvas.move('myhero', hero.x - hero_old_x, hero.y - hero_old_y)
        # printer.canvas.move('myhero', 0, -72)        
        # print('up')
    elif e.keysym == 'Down':
        hero.move('down')
        # printer.drawer(hero)
        printer.canvas.itemconfig(printer.hero_img, image = printer.hero_down)
        printer.canvas.move(printer.hero_img, hero.x - hero_old_x, hero.y - hero_old_y)      
        # print('down')
    elif e.keysym == 'Right':
        hero.move('right')
        printer.canvas.itemconfig(printer.hero_img, image = printer.hero_right)
        printer.canvas.move(printer.hero_img, hero.x - hero_old_x, hero.y - hero_old_y)
        # print('right')
    elif e.keysym == 'Left':
        hero.move('left')
        printer.canvas.itemconfig(printer.hero_img, image = printer.hero_left)
        printer.canvas.move(printer.hero_img, hero.x - hero_old_x, hero.y - hero_old_y)
        # print('left')


printer.canvas.bind("<KeyPress>", on_key_press)

printer.drawer(hero)


printer.root.mainloop()