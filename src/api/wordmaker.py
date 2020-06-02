def concat(word, start, end):
    '''combining words into sentence'''
    sentence= ""
    for i in range(start, end+1):
        if i==start:
            sentence=word[i]
        else:
            sentence= sentence+" "+word[i]
    return sentence

def removeSymbol(word) :
    '''removing symbols from text'''
    nosymbol = []
    symbol = {}

    for i in range(len(word)) :
        if(word[i][-1].lower() == word[i][-1].upper()) : 
            nosymbol.append(word[i][:-1])
            symbol[i] = word[i][-1]
        else :
            nosymbol.append(word[i])
    
    return nosymbol, symbol
