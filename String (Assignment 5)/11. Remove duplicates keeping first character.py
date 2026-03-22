s = input("Enter string: ")
seen = set()
result = ""
for ch in s:
    if ch not in seen:
        result += ch
        seen.add(ch)
print("Result:", result)
