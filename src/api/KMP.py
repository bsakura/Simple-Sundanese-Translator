def fail(pattern) :
    '''Finding border'''
    fail = [0 for i in range(len(pattern))]
    fail[0] = 0

    m = len(pattern)
    j = 0
    i = 1

    while i < m :
        if pattern[j].lower() == pattern[i].lower() :
            fail[i] = j + 1
            i += 1
            j += 1
        elif j > 0 :
            j = fail[j - 1]
        else :
            fail[i] = 0
            i += 1
    return fail


def kmp(teks, pattern):
    border = fail(pattern)
    n = len(teks)
    m = len(pattern)

    i = 0
    j = 0

    while i < n :
        if pattern[j].lower() == teks[i].lower() :
            if j == m - 1 :
                return i - m + 1
            i += 1
            j += 1
        elif j > 0 :
            j = border[j - 1]
        else :
            i += 1    
    return -1
