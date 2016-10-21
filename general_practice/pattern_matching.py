#!/usr/bin/env python

'''

    Find all instances of pattern in text t. 
    Return index of match for each distinct match, or -1 if none.

'''

def find_match_indexes(pattern, text):

    match_locations = []
    pattern_index = 0

    for text_index, char in enumerate(text):

        # end of pattern
        if pattern_index >= len(pattern):
            match_locations.append(text_index - len(pattern))  
            pattern_index = 0

        # another matched text character from pattern 
        if char == pattern[pattern_index]:
            pattern_index += 1

        # not a match. continue but make sure pattern_index is back at 0
        else:
            pattern_index = 0

    return match_locations
