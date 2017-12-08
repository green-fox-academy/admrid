# Given a non-negative int n, return the sum of its digits recursively (no loops). 
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while 
# divide (/) by 10 removes the rightmost digit (126 // 10 is 12).

def summer(n):
    if n > 0 and n < 10:
        return n
    else:
        return (n % 10) + summer(n // 10) 

print(summer(126))
