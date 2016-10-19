#!/usr/bin/env python

from utils import run_tests

# Issues:
# remove list slicing: using list slicing is expensive and works against the nlogn solution.

def merge_sort(data):

    if len(data) == 1:
        return data

    middle = len(data) / 2
    return merge_lists(merge_sort(data[:middle]), merge_sort(data[middle:]))

def merge_lists(l, r):

    merged_list = []

    while l and r:
        if l[0] <= r[0]:
            merged_list.append(l[0])
            if l:
                l = l[1:]
        else:
            merged_list.append(r[0])
            if r:
                r = r[1:]

    if l:
        merged_list.extend(l)

    else:
        merged_list.extend(r)

    return merged_list

if __name__ == '__main__':
    run_tests(merge_sort, num_tests=3, min_list_length=2000, max_list_length=20000)
