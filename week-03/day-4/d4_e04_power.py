# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def topower(base, power):
    if base == 0 or power == 0:
        return 1
    else:
        return base * topower(base, power - 1)

print(topower(3, 4))