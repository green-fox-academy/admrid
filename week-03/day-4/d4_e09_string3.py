# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def addstar(stringi):
    if stringi == '':
        return ''
    # if stringi[0] == 'x':
    # elif stringi[0+1] == ' ':
    #     return stringi[0] + addstar(stringi[1:])
    if stringi[0] == stringi[::-1]:
        return stringi[::-1]
    else:
        return  stringi[0] + '*' + addstar(stringi[1:])
    return stringi[0] + addstar(stringi[1:])

print(addstar('Obviouxslyx you would never actxually use a recursxive solution like xthis this x type, but here it is anyway'))