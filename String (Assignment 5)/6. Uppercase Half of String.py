s = input("Enter string: ")
half = len(s) // 2
new_s = s[:half].upper() + s[half:]
print("Result:", new_s)
