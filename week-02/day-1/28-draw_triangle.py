# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

numi = input("Dobj nekem egy numit ide pajti: ")
numi = int(numi)

for n in range(1, numi +1):
    print("*" * n)