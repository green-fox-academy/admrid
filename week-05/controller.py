from model import *
from view import *

map = Map()

printer = Printer()

for i in range(len(map.map_lista)):
    printer.drawer(map.map_lista[i])

printer.root.mainloop()