from extractor import *
from wordmaker import *
from BM import *
from KMP import *
from RE import *

Ind = extIndoSunda()
Sund = extSundaIndo()


def translateWord (vocab, language, method):
    '''translate each word'''
    if language==0:
        '''Indonesia-Sunda'''
        for tk in Ind:
            if len(tk[0]) == len(vocab):
                if method == 0:
                    idx= kmp(tk[0], vocab)
                elif method == 1:
                    idx= bm(tk[0], vocab)
                elif method == 2:
                    idx= reg(tk[0], vocab)
                
                if idx==0:
                    return(1,tk[1])

    elif language==1:
        '''Sunda-Indonesia'''
        for tk in Sund:
            if len(tk[0]) == len(vocab):
                if method == 0:
                    idx= kmp(tk[0], vocab)
                elif method == 1:
                    idx= bm(tk[0], vocab)
                elif method == 2:
                    idx= reg(tk[0], vocab)
                
                if idx==0:
                    return(1,tk[1])

    return (0, vocab)

    
def translate(text, language, method):
    subject=['anjeun', 'anjeunna', 'maneh', 'manehna', 'urang', 'abdi', 'aing', 'ieu']
    question = ['saha', 'naon', 'mengapa', 'ayeuna']
    word= text.split(' ')
    nosymbol, symbol= removeSymbol(word)

    penekanan= False

    translatedWord=[]
    i=0
    while i<(len(word)):
        for j in range (len(word)-1, i-1, -1):
            vocab=concat(nosymbol, i, j)
            translatedVocab=vocab
            translated=translateWord(vocab, language, method)
            if translated[0] == 1:
                translatedVocab=translated[1]

                if j in symbol:
                    translatedVocab=translatedVocab+symbol[j]
                break

        if translated[0] == 0:
            if language ==1 and translatedVocab=='teh':
                if word[i-1] in subject:
                    i+=1
                    continue

        translatedVocab = translatedVocab.split(' ')
        for k in range(len(translatedVocab)):
            translatedWord.append(translatedVocab[k])

        if language==0:
            '''Adding penekanan'''
            if translatedWord[-1] in subject and not penekanan:
                translatedWord.append('teh')
                penekanan=True
            elif translatedWord[-1] in question and not penekanan:
                translatedWord.insert(i,'teh')
                penekanan=True
                
        i=j+1

    return concat(translatedWord, 0, len(translatedWord)-1)


