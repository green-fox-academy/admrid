from model import *
from view import *

map = Map()
hero = Hero()

printer = Printer()

for i in range(len(map.map_lista)):
    printer.drawer(map.map_lista[i])
§
printer.drawer(hero.)

printer.root.mainloop()