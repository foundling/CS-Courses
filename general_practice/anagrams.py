'''
Two strings are anagrams if they are written using the same exact letters, ignoring space, punctuation and capitalization.
'''

def anagram_test(a,b):

    w1 = map(str.lower, sorted(a))
    w2 = map(str.lower, sorted(b))

    are_anagrams = True

    for index, char in enumerate(w1):
        if char != w2[index]:
            are_anagrams = False
            break

    return are_anagrams
