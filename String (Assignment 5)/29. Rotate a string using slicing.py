s = input("Enter string: ")
n = int(input("Enter rotation amount: "))
rotated = s[n:] + s[:n]
print("Rotated string:", rotated)
