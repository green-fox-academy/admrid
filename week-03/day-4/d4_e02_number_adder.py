# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

def counter(n):
    if n == 0:
        return n
    else:
        print(n)
        return(n + counter(n-1))

print(counter(10))
