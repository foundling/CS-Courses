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
