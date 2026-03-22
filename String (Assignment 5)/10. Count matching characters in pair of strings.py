s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
matches = sum(1 for a, b in zip(s1, s2) if a == b)
print("Matching characters:", matches)
