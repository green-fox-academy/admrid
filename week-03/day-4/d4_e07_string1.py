# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

stringem = 'Obviouxslyx you would never actxually use a recursxive solution like xthis this x type, but here it is anyway'

def replaceChar(inval, old, new):
    if inval == '':
        return ''
    if inval[0] == old:
        return new + replaceChar(inval[1:], old, new)
    return inval[0] + replaceChar(inval[1:], old, new)

print(replaceChar('Obviouxslyx you would never actxually use a recursxive solution like xthis this x type, but here it is anyway', 'x', 'y'))