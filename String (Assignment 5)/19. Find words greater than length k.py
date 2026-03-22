s = input("Enter string: ")
k = int(input("Enter length k: "))
words = s.split()
result = [w for w in words if len(w) > k]
print("Words longer than", k, ":", result)
