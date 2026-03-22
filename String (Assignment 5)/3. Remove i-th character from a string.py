s = input("Enter string: ")
i = int(input("Enter index to remove: "))
new_s = s[:i] + s[i+1:]
print("Result:", new_s)
