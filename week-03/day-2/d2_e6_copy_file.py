
# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

def copier(path1, path2):
    myfile1 = open(path1)
    myfile2 = open(path2, 'w')
    text = myfile1.read()
    myfile2.write(text)
    myfile1.close
    myfile2.close
    return True

print(copier('file5.txt', 'file6.txt'))