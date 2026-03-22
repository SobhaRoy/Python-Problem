binary = input("Enter binary number: ")
num = 0
for ch in binary:
    num = num * 2 + (ord(ch) - ord('0'))
print("Decimal:", num)
