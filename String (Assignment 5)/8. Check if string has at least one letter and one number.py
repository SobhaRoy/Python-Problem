s = input("Enter string: ")
has_letter = any(ch.isalpha() for ch in s)
has_digit = any(ch.isdigit() for ch in s)
print("Contains letter and number:", has_letter and has_digit)
