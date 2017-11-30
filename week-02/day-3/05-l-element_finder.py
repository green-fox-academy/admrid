# Check if the list contains "7" if it contains print "Hoorray" otherwise print "Noooooo"

numbers = [1, 2, 3, 4, 5, 6, 8];
nono = []

for number in numbers:
    if number == 7:
        seven = True
        break 
    else:
        seven = False

if seven == True:
    print("Hoorray")
else:
    print("Noooooo")
