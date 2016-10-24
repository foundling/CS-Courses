#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

    Find all indexes where pattern is found in text. 

'''

def find_match_indexes(pattern, text):

    # compare pattern with text, moving along the text index
    # until you reach index where the pattern could no longer fit
    # in the text.  this index is (len(text) - len(pattern) - 1)

    tlen, plen = len(text), len(pattern)
    match_indexes = []

    if plen > tlen:
        return -1

    for tindex, tchar in enumerate(text):

        # if pattern couldn't possibly exist in remaining 
        # sequence, break.
        if tindex == tlen - plen + 1:
            print 'stopping at tindex' , tindex
            break

        matched = True

        for pindex, pchar in enumerate(pattern):
            if pchar != text[tindex + pindex]: 
                matched = False
                break

        if matched:
            match_indexes.append(tindex)
    
    return match_indexes

p = 'bar'
t = 'barbar'
print p
print t
print find_match_indexes(p,t)
