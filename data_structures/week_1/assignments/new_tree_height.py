# python 2

'''
Alex Ramsdell
Coursera Data Structures
Week 1 Programming Assignment, Problem #2 Compute Tree Height

Input: first line, N, number of vertices in the tree. Second line, a space-delimited list of integers, L, 
from L[0] to L[n-1], where the index represents a node, and the value at that index represents the node's parent index.
If the value at the index is -1, that represents the root node.

Output: tree height

'''

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def build_tree(parents, n):

    tree = {}
    key = None
    for i in range(n):
        key = parents[i]
        if key in tree:
            tree[key].append(i)
        else:
            tree[key] = [i]
    return tree

def tree_height(tree, key):

    if key not in tree:
        return 0
    else:
        children = tree[key]
        return 1 + max([tree_height(tree, c) for c in children])

def main():

    n = int(raw_input().strip())
    parents = [ int(num) 
                for num 
                in raw_input().split() ]
    tree = build_tree(parents, n)
    root_key = -1
    height = tree_height(tree, root_key)
    print height

threading.Thread(target=main).start()
