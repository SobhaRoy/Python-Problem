import string
s = input("Enter string: ")
special = any(ch in string.punctuation for ch in s)
print("Contains special character:", special)
