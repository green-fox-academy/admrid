# - Create a function called `printer`
#   which prints the input parameters
#   (can have multiple number of arguments)

def printer(*args):
    print("Hello, ", args)


printer(1, 2, 3)