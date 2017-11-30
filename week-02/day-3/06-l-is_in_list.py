# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
to_check = [4, 8, 12, 16]

# def check(list_of_numbers, to_check):
#     for number1 in to_check:
#         number2 = number1
#         for number2 in list_of_numbers:
#             if number1 != number2:
#                 print(number2)
#             elif number1 == number2:
#                 print(number1)

def check(list_of_numbers, to_check):
    for number1 in to_check:
        if number1 in list_of_numbers:
            return True
        else:
            return False

print(check(list_of_numbers, to_check))