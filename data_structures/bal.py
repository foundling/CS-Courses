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
