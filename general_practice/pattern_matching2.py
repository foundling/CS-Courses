#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

    Find all indexes where pattern is found in text. 

'''

def find_match_indexes(pattern, text):

    pattern_index, pattern_len = 0, len(pattern)
    match_indexes = []

    if pattern_len > len(text):
        raise ValueError('The pattern must be equal or shorter in length than the text')

    for tindex, tchar in enumerate(text):

        if pattern_index == pattern_len:

            match_indexes.append(tindex - pattern_len)

            if tchar == pattern[0]:
                pattern_index = 1

            else:
                pattern_index = 0

        else:

            if tchar == pattern[pattern_index]:
                pattern_index += 1

            else:
                if tchar == pattern[0]:
                    pattern_index = 1

                else:
                    pattern_index = 0

    if pattern_index == pattern_len:
        match_indexes.append(tindex + 1 - pattern_len)  

    return match_indexes

p = 'bar'
t = 'barbarbbarbar'

print("matching for {} in {}".format(p,t))
print(find_match_indexes(p,t))
