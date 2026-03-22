a = input("Enter string a: ")
b = input("Enter string b: ")

missing = [ch for ch in a if ch not in b]
is_balanced = len(missing) == 0

print("Balanced:", is_balanced)
if missing:
    print("Missing characters:", missing)
