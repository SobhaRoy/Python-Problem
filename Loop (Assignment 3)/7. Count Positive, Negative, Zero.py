pos = neg = zero = 0

while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        zero += 1
        break
    elif num > 0:
        pos += 1
    else:
        neg += 1

print("Positive:", pos)
print("Negative:", neg)
print("Zero:", zero)
