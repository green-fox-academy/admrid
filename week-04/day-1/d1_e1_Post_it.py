'''Create a PostIt class that has
a background_color
a text on it
a text_color

Create a few example post-it objects:
an orange with blue text: "Idea 1"
a pink with black text: "Awesome"
a yellow with green text: "Superb!"'''

class Postit(object):
    
    def __init__(self, name, bg_color, text, text_color):
        self.name = name
        self.bg_color = bg_color
        self.text = text
        self.text_color = text_color
        print(self.name, self.bg_color, self.text, self.text_color)
    
Idea_1 = Postit('Idea 1', 'orange', 'idea of the idea', 'blue')
Awesome = Postit('Awesome', 'pink', 'Awesome of the Awesome', 'black')
Superb = Postit('Superb', 'yellow', 'Superb of the Superb', 'green')