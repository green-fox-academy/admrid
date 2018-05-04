# Adds a and b, returns as result
def add(a, b):
    result = a + b
    return result

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return c
    elif c > a and c > b:
        return c

# Returns the median value of a list given as param
def median(pool):
    # return pool[(len(sorted(pool)) - 1) / 2)]
    n = len(pool)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(pool)[n//2]
    else:
            return sum(sorted(pool)[n//2-1:n//2+1])/2.0

# Returns true if the param is a vovel
def is_vowel(char):
    vowelchars = 'aeiouéáőűöüóí'
    if char not in vowelchars:
        return False
    else:
        return True

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    tevenew = ''
    for char in teve:
        if is_vowel(char):
            tevenew += (char+'v'+char)
        else:
            tevenew += char
    return tevenew
