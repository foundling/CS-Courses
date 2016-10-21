#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

    Find all instances of pattern in text t. 
    Return tuple of indexes indicating the location of each distinct match or None if none are found.

'''

def find_match_indexes(pattern, text):

    match_locations = []
    pattern_index = 0
    pattern_length = len(pattern)

    for text_index, char in enumerate(text):

        # check for end of pattern
        if pattern_index >= pattern_length:
            match_locations.append(text_index - pattern_length)  
            pattern_index = 0

        # also, check for another matched text character from pattern 
        if char == pattern[pattern_index]:
            pattern_index += 1

        # or it's not a match. so reset pattern_index 
        else:
            pattern_index = 0

    # check if pattern matches end of text
    if pattern_index == pattern_length:
        print text_index, pattern_length
        match_locations.append(text_index - (pattern_length - 1))  

    return match_locations
