water_with = 0          
towater = []
trees = []
flowers = []


class Plant():
    def __init__(self, plant, color, water_level=0):
        self.color = color
        self.water_level = water_level


#def Garden():
    
    '''
    def flower_planter(name, color,):
        flower_name = name
        flower_color = color
        flower_name = Flower(flower_color)
    ''' 
        
def what_to_water(self):
    for i in trees:     #check what_to_water
        if i.water_level < 10:
            towater.append(i)
    for o in flowers:   #check what_to_water
        if o.water_level < 5:
            towater.append(i)

def watering(self, water_amount):
    self.water_amount = water_amount
    water_with = self.water_amount / len(towater)   #water
    for i in towater:
        if self.plant == 'tree':
            self.watered += 0,4 * water_with
        else:
            self.watered += 0,7 * water_with

class Tree(Plant):
    def __init__(self, plant, color, water_level=0):
        super().__init__(plant, color, water_level)
        #self.plant = plant #jobb lenne helyett instance()-t hasznalni
        #self.watered += 0,4 * water_with
    

class Flower(Plant):
    def __init__(self, plant, color, water_level=0):
        super().__init__(plant, color, water_level)
        #self.plant = plant #jobb lenne helyett instance()-t hasznalni
        #self.watered += water * 0,7


flower1 = Flower('flower','yellow')
trees.append(flower1) 
flower2 = Flower('flower','blue')
trees.append(flower2)
tree1 = Tree('tree','purple')
trees.append(tree1) 
tree2 = Tree('tree','orange')
trees.append(tree2) 
