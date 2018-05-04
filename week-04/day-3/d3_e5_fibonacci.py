def fibonacci_maker(n):
    if n < 2:
        return n
    else:
        return (fibonacci_maker(n-1) + fibonacci_maker(n-2))

# print(fibonacci_maker(4))