# python 2

'''

Michael Levin says:

If you just build the tree from the input provided and then implement a recursive function 
to find height almost the same way it was described in the lectures for binary trees, 
you will solve the problem, and the solution will be fast, O(n).

'''

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def tree_height(tree):
    if not tree:
        return 0
    return 1 + max(map(tree_height, children))

def build_tree(parents, n):

    tree = {}
    for vertex in range(n):
        node = {'parent': None, 'children': []}
        i = vertex
        while i != -1:



def main():
    n = int(raw_input().strip())
    parents = [ int(num) 
                for num 
                in raw_input().split() ]
    tree = build_tree(parents, n)
    print tree_height(tree)

threading.Thread(target=main).start()
