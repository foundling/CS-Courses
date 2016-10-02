# python 2
'''
Michael Levin - If you just build the tree from the input provided and then implement a recursive function to find height almost the same way it was described in the lectures for binary trees, you will solve the problem, and the solution will be fast, O(n).
'''

import sys, threading
sys.setrecursionlimit(10**7) 
threading.stack_size(2**27)  

def tree_height(n, parents):

    maxHeight = 0
    cache = {}

    for vertex in range(int(n)):
        height = 0
        i = vertex
        while i != -1:
            if parents[i] in cache:
                height += cache[ parents[i] ] + 1
                break
            else:
                height += 1
                cache[ parents[i] ] = height
                i = parents[i]
        maxHeight = max(maxHeight, height);

    print cache
    return maxHeight;

def main():
    n = int(raw_input().strip())
    parents = [ int(num) 
                for num 
                in raw_input().split() ]
    print tree_height(n, parents)

threading.Thread(target=main).start()
