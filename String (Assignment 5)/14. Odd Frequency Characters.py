from collections import Counter
s = input("Enter string: ")
freq = Counter(s)
odd_chars = [ch for ch, f in freq.items() if f % 2 != 0]
print("Characters with odd frequency:", odd_chars)
