# Open a file called "my-file.txt"
# Write your name in it as a single line
# If the program is unable to write the file,
# then it should print an error message like: "Unable to write file: my-file.txt"

try:
    myfili = open('myfile.txt', 'w')
    myfili.write('adam')    
except:
    print('Unable to write file: my-file.txt')
finally:
    myfili.close