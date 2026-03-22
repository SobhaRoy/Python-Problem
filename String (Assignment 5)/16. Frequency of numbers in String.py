s = input("Enter string: ")
numbers = [ch for ch in s if ch.isdigit()]
from collections import Counter
freq = Counter(numbers)
print("Number frequencies:", dict(freq))
