s = input("Enter string: ")
for i in range(1, len(s)+1):
    rotated = s[i:] + s[:i]
    if rotated == s:
        print("Minimum rotations to get original:", i)
        break
