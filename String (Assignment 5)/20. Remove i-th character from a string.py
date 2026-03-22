# Input string
s = input("Enter a string: ")

# Input index to remove
i = int(input("Enter the index (0-based) of character to remove: "))

# Remove i-th character
if 0 <= i < len(s):
    new_s = s[:i] + s[i+1:]
    print("Resulting string:", new_s)
else:
    print("Invalid index! Index should be between 0 and", len(s)-1)
