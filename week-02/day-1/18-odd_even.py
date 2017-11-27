# Write a program that reads a number form the standard input,
# Than prints "Odd" if the number is odd, or "Even" it it is even.

numi = input("Type a number here ")
numi = int(numi)

if numi % 2 == 0:
    print("Even")
else:
    print("Odd")