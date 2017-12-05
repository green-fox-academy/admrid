# Create a method that decrypts reversed-lines.txt

def decrypt(file_name):
    textfile = open(file_name)
    textdec = open('file9dec.txt', 'w')
    textorig = textfile.readlines()
    # textorig.append('\n')
    text = ''
    for i in reversed(range(len(textorig))):
        text += textorig[i]
    textdec.write(text)
    textfile.close
    textdec.close
    return text

print(decrypt('file9.txt'))