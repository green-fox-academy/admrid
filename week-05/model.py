from random import randint

class Tile():
    def __init__(self, imagefile, x, y, can_go_through):
        self.imagefile = imagefile
        self.x = x
        self.y = y
        self.can_go_through = can_go_through

class FloorTile(Tile):
    def __init__(self, x, y):
        super().__init__('assets/floor.gif', x, y, True)
        
class WallTile(Tile):
    def __init__(self, x, y):
        super().__init__('assets/wall.gif', x, y, False)

class Map():

    def __init__(self):
        self.map_transp_lista = [
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 1, 1, 1, 0, 0, 1],
            [0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 1, 1, 0, 0]]

        self.map_lista = []
        # self.floor = FloorTile()
        # self.wall = WallTile()
        for i in range(len(self.map_transp_lista)):
            for j in range(len(self.map_transp_lista[i])):
                if self.map_transp_lista[i][j] == 0:
                    self.map_lista.append(FloorTile(i*72, j*72))
                else:
                    self.map_lista.append(WallTile(i*72, j*72))
        # print(self.map_lista)

class Char():
    # d6 = d6 is a random number between 1 and 6 aka 6 sided die rol
    
    def __init__(self, imagehero1, x, y, hp, dp, sp):
        self.imagehero1 = imagehero1
        self.x = x
        self.y = y
        self.hp = hp
        self.dp = dp
        self.sp = sp

    def d6():
        dice_num = randint(1, 6)

class Hero(Char):
    def __init__(self):
        super().__init__('assets/wall.gif', 20 + 3 * randint(1, 6), 2 * randint(1, 6), 5 + randint(1, 6))
        # HP: 20 + 3 * d6
        # DP: 2 * d6
        # SP: 5 + d6

class Monster(Char):
    def __init__(self):
        super().__init__('assets/wall.gif', 2 * x * randint(1, 6) (+ randint(1, 6)), x/2 * randint(1, 6) (+ randint(1, 6)/2), x * randint(1, 6) (+x))


hero = Hero()
print(hero.d6)