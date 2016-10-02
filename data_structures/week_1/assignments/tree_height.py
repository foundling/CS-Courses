# python 2
'''
Michael Levin - If you just build the tree from the input provided and then implement a recursive function to find height almost the same way it was described in the lectures for binary trees, you will solve the problem, and the solution will be fast, O(n).
'''

import sys, threading
sys.setrecursionlimit(10**7) 
threading.stack_size(2**27)  

def tree_height(n, parent):

    maxHeight = 0
    cache = {}

    for vertex in range(int(n)):
        if parent[vertex] in cache:
            height = cache[parent[vertex]]
        else:
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = parent[i]
            cache[parent[vertex]] = height
            maxHeight = max(maxHeight, height);

    return maxHeight;

def main():
    _ = raw_input()
    parent = [ int(n) 
                for n 
                in raw_input().split() ]
    n = len(parent)
    print tree_height(n, parent)

threading.Thread(target=main).start()
