# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

def liner(stringi):    
    try:
        thestring = open(stringi)
        lines = thestring.readlines()
        nolitems = 0
        for listitems in lines:
            nolitems += 1
    except FileNotFoundError:
        nolitems = 0
    finally:
        thestring.close
        return nolitems


print(liner('filika2.txt'))