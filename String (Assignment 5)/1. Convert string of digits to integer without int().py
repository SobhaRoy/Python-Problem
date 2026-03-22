s = input("Enter digits: ")
num = 0
for ch in s:
    num = num * 10 + (ord(ch) - ord('0'))
print("Integer:", num)
