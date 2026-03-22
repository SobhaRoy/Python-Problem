from collections import Counter
s = input("Enter string: ")
freq = Counter(s)
max_char = max(freq, key=freq.get)
print("Max frequency character:", max_char)
