# Write a program that asks for an integer that is a distance in kilometers,
# then it converts that value to miles and prints it

distance = input("Type your distance: ")
distance = int(distance)
distance = distance * 0.62
print(str(distance) + " miles")