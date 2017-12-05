# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

divisor = int(input('Yo gimme a numbi pls: '))

def the_divider():
    try:
        result = 10 / divisor
        print(result)
    except ZeroDivisionError:
        print('fail - Héló Ju Kán\'t divide by zero!')

the_divider()