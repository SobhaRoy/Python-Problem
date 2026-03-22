s = input("Enter mixed string: ")
digits = [int(ch) for ch in s if ch.isdigit()]

if digits:
    total = sum(digits)
    avg = total / len(digits)
    maximum = max(digits)
    minimum = min(digits)
    print("Sum:", total)
    print("Average:", avg)
    print("Max digit:", maximum)
    print("Min digit:", minimum)
else:
    print("No digits found in the string")
