#python2 

'''
Status: 'Good job! (Max time used: 0.08/1.00, max memory used: 9519104/536870912.)' 

Alex Ramsdell
Coursera Data Structures Week 1 Programming Assignment

Check Brackets in the Code

Constraints: the length of S is at least 1 and at most 10^5.
Input:  one string S which consists of big and small latin letters, digits, punctuation marks and brackets from the set []{}().
Output: Output 'Success' if the code uses brackets correctly and the 1-based index of the first unmatched closing bracket otherwise. 

Cases: Empty String, Missing closing, missing opening, incorrect closing.

empty: '' -- stack empty
missing closing bracket: [[] -- stack not empty at end of code
missing opening bracket: ]]) -- stack underflow 
incorrect closing: [} -- stack pop mismatch

'''

def top(stack):
    return None if empty(stack) else stack[-1][0] 

def empty(stack):
    return not len(stack)

def stack(code):

    stack = []
    is_valid = True
    error_index = -1
    opening = [
        '(',
        '[',
        '{'
    ]
    closing = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for index, char in enumerate(code):

        if char in opening:
            stack.append((char, index))

        elif char in closing:

            # nothing to pop (closing bracket before opening)
            if empty(stack):
                error_index = index
                is_valid = False
                break

            # mismatched closing bracket
            # give current index in both cases 
            elif top(stack) != closing[char]:
                error_index = index
                is_valid = False
                break

            # its a match
            elif top(stack) == closing[char]:
                stack.pop()


    if is_valid and not empty(stack):
        is_valid = False
        char, error_index = stack.pop()

    return is_valid, error_index + 1

code_string = raw_input()
is_valid, error_index = stack(code_string)
print 'Success' if is_valid else error_index  
