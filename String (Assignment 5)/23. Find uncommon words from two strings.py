s1 = set(input("Enter first string: ").split())
s2 = set(input("Enter second string: ").split())
uncommon = list(s1.symmetric_difference(s2))
print("Uncommon words:", uncommon)
