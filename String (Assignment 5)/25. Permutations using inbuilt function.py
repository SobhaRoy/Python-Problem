from itertools import permutations
s = input("Enter string: ")
perm = [''.join(p) for p in permutations(s)]
print("Permutations:", perm)
