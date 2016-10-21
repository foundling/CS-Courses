#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

    Find all instances of pattern in text t. 
    Return tuple of indexes indicating the location of each distinct match or None if none are found.

'''

def find_match_indexes(pattern, text):

    match_locations = []
    pattern_index, pattern_length = 0, len(pattern)

    for text_index, char in enumerate(text):

        # check for single character match -- should go before checking for full pattern match
        if pattern_index < pattern_length and char == pattern[pattern_index]:
            pattern_index += 1

        # check for complete match
        elif pattern_index == pattern_length - 1:
            match_locations.append(text_index - pattern_index)
            pattern_index = 0

        # no match, reset accrued pattern index
        else:
            pattern_index = 0
            

    return match_locations
