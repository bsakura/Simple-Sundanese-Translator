class last_occurrence(object):
    '''finding the last occurence'''
    def __init__(self, pattern, alphabet):
        self.occurrences = dict()
        for letter in alphabet:
            self.occurrences[letter] = pattern.rfind(letter)
    def __call__(self, letter):
        return self.occurrences[letter]


def bm(text, pattern):
    alphabet = set(text)
    last = last_occurrence(pattern, alphabet)
    m = len(pattern)
    n = len(text)
    i = m - 1  
    j = m - 1 
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = last(text[i])
            i = i + m - min(j, 1+l)
            j = m - 1 
    return -1
