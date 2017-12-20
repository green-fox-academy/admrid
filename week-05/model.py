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

        for i in range(len(self.map_transp_lista)):
            for j in range(len(self.map_transp_lista[i])):
                if self.map_transp_lista[i][j] == 0:
                    self.map_lista.append(FloorTile(i*72, j*72))
                else:
                    self.map_lista.append(WallTile(i*72, j*72))
        # print(self.map_lista)

class Char():
    
    def __init__(self, imagefile, x, y, hp, dp, sp):
        self.imagefile = imagefile
        self.x = x
        self.y = y
        self.hp = hp
        self.dp = dp
        self.sp = sp

    def d6(self):
        return randint(1, 6)

    def move(self, direction):
        self. direction = direction
        if direction == 'up':
          self.y -= 72
        if direction == 'down':
          self.y += 72
        if direction == 'right':
          self.x += 72
        if direction == 'left':
          self.x -= 72

class Hero(Char):
    def __init__(self):
        super().__init__('assets/hero-down.gif', 0, 0, 20 + 3 * self.d6(), 2 * self.d6(), 5 + self.d6())
        # HP: 20 + 3 * d6
        # DP: 2 * d6
        # SP: 5 + d6


class Monster(Char):
    def __init__(self):
        super().__init__('assets/hero-down.gif', x, y, 2 * self.d6() (+ self.d6()), 2 * self.d6() (+ self.d6()/2), self.d6())
        # ORIGINAL VALUES:
        # super().__init__('assets/hero-down.gif', x, y, 2 * x * self.d6() (+ self.d6()), x/2 * self.d6() (+ self.d6()/2), x * self.d6() (+x))