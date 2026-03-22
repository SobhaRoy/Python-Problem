# Input a five-digit number
num = input("Enter a five-digit number: ")

# Add 1 to each digit
new_num = ""
for digit in num:
    new_digit = (int(digit) + 1) % 10  # Use modulo 10 for digit 9
    new_num += str(new_digit)

print("New Number:", new_num)
