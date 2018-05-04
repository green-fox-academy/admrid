def string_to_dict(string = ''):
    stringdict = {}
    for letter in string:
        if letter not in stringdict:
            stringdict[letter] = 1
        else:
            stringdict[letter] += 1
    return stringdict
        # SOLUTION W 2 FORS
        # for i in range(len(stringdict)):
        #     if letter == stringdict[i]:
        #         stringdict['letter'] = '+=1'    
        # else:
        #     stringdict['i'] = 'string[1]'