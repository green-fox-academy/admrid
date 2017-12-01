import random

def guess_my_num():
    our_range = []
    your_range = 0
    your_range = int(input('Guess My Number: Type a number to set the range: '))
    our_range.extend(range(0, your_range))
    my_num = random.randint(0, our_range[-1])
    your_num = int(input('I\'ve a number between 0 and ' + str(your_range) + '. Guess shich one is it: '))
    life = 5
    while life > 0:
        if your_num == my_num:
            print('Congrats, You won!')
            return
        elif your_num < my_num:
            life -= 1   
            your_num = int(input('Too low. You have ' + str(life) + ' lives left.\nGuess another one: '))      
        elif your_num > my_num:
            life -= 1   
            your_num = int(input('Too high. You have ' + str(life) + ' lives left.\nGuess another one: '))

guess_my_num()