def can_be_empty(s):
    while s:
        first = s[0]
        s = s.replace(first, '')
    return len(s) == 0

s = input("Enter string: ")
print("Can become empty:", can_be_empty(s))
