# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

def counter(ears, bunnynum):
    if bunnynum == 0:
        return 0
    else:
        return ears + counter(ears, bunnynum - 1)

print(counter(2, 100))