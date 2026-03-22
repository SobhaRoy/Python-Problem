s = input("Enter string: ")
i = 0
result = []
while i < len(s):
    count = 1
    while i + 1 < len(s) and s[i] == s[i+1]:
        count += 1
        i += 1
    result.append((s[i], count))
    i += 1
print("Consecutive character frequencies:", result)
