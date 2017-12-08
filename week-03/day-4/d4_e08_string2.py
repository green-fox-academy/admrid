# Given a string, compute recursively a new string where all the 'x' chars have been removed.

stringem = 'Obviouxslyx you would never actxually use a recursxive solution like xthis this x type, but here it is anyway'

def replaceChar(inval):
    if inval == '':
        return ''
    if inval[0] == 'x':
        return  '' + replaceChar(inval[1:])
    return inval[0] + replaceChar(inval[1:])

print(replaceChar('Obviouxslyx you would never actxually use a recursxive solution like xthis this x type, but here it is anyway'))