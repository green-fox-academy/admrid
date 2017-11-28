# - Create a function called `factorio`
#   that returns it's input's factorial

def factorio(numb):
    summ = 1
    for n in range(1, numb + 1):
        summ = summ * n
    return summ

print(factorio(5))