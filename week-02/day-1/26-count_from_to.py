# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
# 
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5

numi1 = input("Dobj nekem egy numbit ide: ")
numi1 = int(numi1)
numi2 = input("Dobj nekem +egy numbit ide: ")
numi2 = int(numi2)

if numi1 >= numi2:
    print("The second number should be bigger")
elif numi1 < numi2:
    for n in range(numi1, numi2, 1):
        print(n)