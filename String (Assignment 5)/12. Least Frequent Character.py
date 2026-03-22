from collections import Counter
s = input("Enter string: ")
freq = Counter(s)
least_char = min(freq, key=freq.get)
print("Least frequent character:", least_char)
