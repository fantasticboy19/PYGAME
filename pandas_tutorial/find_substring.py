a = 'abcdef'
b = 'absdsadfdaskkfabcdejfjd'


def is_substring(s, t):
    t = iter(t)
    print(all(c in t for c in s))



def is_substring2(s, t):
    print(s in t)


is_substring2(a, b)