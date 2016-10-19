#!/usr/bin/env python

# Test Data Generator to test Algorithm Correctness 

import random

def run_tests(f, num_tests=20, value_limit=100, min_list_length=1, max_list_length=10):

    # run f on NUM_TESTS data sets of max length MAX_LIST_LENGTH whose values are less than VALUE_LIMIT

    data_sets = [
                    [ 
                        random.randrange(value_limit)  
                        for x 
                        in range(random.randrange(min_list_length, max_list_length)) 
                    ] 

                    for y
                    in range(num_tests)
                ]
    for data_set in data_sets:
        print f(data_set)
