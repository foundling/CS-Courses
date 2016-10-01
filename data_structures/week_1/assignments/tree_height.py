# python 2

'''

Alex Ramsdell
Coursera Data Structures
Week 1, Problem 2: Compute Tree Height

Constraints: N is greater than 1 and less than 10^5.

Input: first line is number of vertices, N. second line contains n ints from -1 to 1 where each int is a parent of a vertex. 
If Ni is -1, Ni is the root. Otherwise, it's the index of the root. 

Output: The height of the tree.

4 -1 4 1 1

index in array = which node. value = index of the parent.

nodes 0 and 2 are children of 4.
node 1 is child of null, aka the root.
node 3 and 4 are child of node 1.

'''

def tree_height():
    pass

def main():

    N = raw_input()
    parents = [ int(n) 
                for n 
                in raw_input().split() ]

if __name__ == '__main__':
    main()
