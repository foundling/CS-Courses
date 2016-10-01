'''
Alex Ramsdell
Coursera Data Structures Week 1 Programming Assignment

Constraints: the length of S is at least 1 and at most 10^5.
Input:  one string 𝑆 which consists of big and small latin letters, digits, punctuation marks and brackets from the set []{}().
Output: Output 'Success' if the code uses brackets correctly and the 1-based index of the first unmatched closing bracket otherwise. 

'''
code_string = raw_input()

def stack(code):
    stack = []
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

    for c in code:

        if c in opening:
            stack.append(c)

        elif c in closing:

            if not len(stack): 

                print 'invalid'
                return;

            if closing[c] == stack[-1]:
                stack.pop()
            else:
                print 'invalid'
                return

    print 'valid' if not len(stack) else 'invalid'

code = raw_input('enter your code for me to balance:').strip()
stack(code)
