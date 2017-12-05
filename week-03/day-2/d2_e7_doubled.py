# Create a method that decrypts the duplicated-chars.txt

def decrypt(file_name):
    textfile = open(file_name)
    textdec = open('file7dec.txt', 'w')
    textorig = textfile.read()
    text = ''
    for i in range(len(textorig)):
        if i%2 == 0:
            text += textorig[i]
    textdec.write(text)
    textfile.close
    textdec.close
    return text

print(decrypt('file7.txt'))