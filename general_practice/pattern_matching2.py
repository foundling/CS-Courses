#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

    Find all indexes where pattern is found in text. 

'''

def find_match_indexes(pattern, text):

    pattern_index = 0
    pattern_len = len(pattern)
    match_indexes = []

    # two essential concerns: finding a match, updating pattern index

    for tindex, tchar in enumerate(text):

        # recognize a match
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
                pattern_index = 0

    # after loop, check for recognized pattern at 'virtual index' 
    if pattern_index == pattern_len:
        match_indexes.append(tindex + 1 - pattern_len)  

    return match_indexes

p = 'bar'
t = 'a barbar can cut hair at the bar'
t = 'barbarbarbar'
print p
print t
print find_match_indexes(p,t)
