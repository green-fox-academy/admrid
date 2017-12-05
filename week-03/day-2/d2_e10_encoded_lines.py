# Create a method that decrypts encoded-lines.txt
# def decrypt(file_name):
#     textfile = open(file_name)
#     textdec = open('file10dec.txt', 'w')
#     textorig = textfile.read()
#     text = ''
#     for i in textorig:
#         charval = ord(i)
#         text += chr(charval - 1)
#     textdec.write(text)
#     textfile.close
#     textdec.close
#     return text

# print(decrypt('file10.txt'))

def decrypt(file_name):
    textfile = open(file_name)
    textdec = open('file10dec.txt', 'w')
    textlist = textfile.readlines()
    # miért nem definiálhatom ezt itt?: textlines = ''
    for line in textlist:
        textlines = ''
        for char in line:
            if char == ' ':
                textlines += ' '
            else:
                charval = ord(char)
                textlines += chr(charval - 1)
        textdec.write(textlines + '\n')
    textfile.close
    textdec.close
    return 'Yes'

print(decrypt('file10.txt'))