# - Write a function called `sum` that sum all the numbers
#   until the given parameter

def sum(numb):
    summ = 0
    for n in range(1, numb + 1):
        summ = summ + n
    return summ

print(sum(5))