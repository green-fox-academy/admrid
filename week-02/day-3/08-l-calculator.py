# Create a simple calculator application which does read the parameters from the prompt 
# and prints the result to the prompt. 

# It should support the following operations: 
# +, -, *, /, % and it should support two operands. 

# The format of the expressions must be: {operation} {operand} {operand}. 
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit

def calc(operation, operand1, operand2):
    if operation == '+':
        return operand1 + operand2
    if operation == '-':
        return operand1 - operand2
    if operation == '*':
        return operand1 * operand2
    if operation == '/':
        return operand1 / operand2
    if operation == '//':
        return operand1 // operand2

inplist = []

def getinput():
    inp = input('Please type in the expression:')
    for content in inp:
        if content != ' ':
            inplist.append(content)
    operation = inplist[0]
    operand1 = int(inplist[1])
    operand2 = int(inplist[2])
    print(calc(operation, operand1, operand2))
    
    
getinput()
