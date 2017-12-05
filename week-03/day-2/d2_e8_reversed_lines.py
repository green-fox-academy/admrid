# Create a method that decrypts reversed-lines.txt

# def decrypt(file_name):
#     textfile = open(file_name)
#     textdec = open('file8dec.txt', 'w')
#     textorig = textfile.read()
#     text = ''
#     for i in reversed(range(len(textorig))):
#         text += textorig[i]
#     textdec.write(text)
#     textfile.close
#     textdec.close
#     return text

# print(decrypt('file8.txt'))

def decrypt(file_name):
    textfile = open(file_name)
    textdec = open('file8dec.txt', 'w')
    textorig = textfile.readlines()
    text = ''
    for lines in textorig:
        textdec.write(lines[::-1])
        # for i in lines[::-1]:
        #     text += lines[i]
    # textdec.write(text)
    textfile.close
    textdec.close

decrypt('file8.txt')