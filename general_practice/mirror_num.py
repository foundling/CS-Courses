def is_mirror_pythonic(n):
    s = str(n)
    return s[::-1] == s

def is_mirror(n):
    s, rv = str(n), True
    for i in range(len(s) / 2):
        #print -i - 1
        if s[-i - 1] != s[i]:
            rv = False
            break
    return rv


