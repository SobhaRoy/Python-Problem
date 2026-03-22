# Input amount to withdraw in hundreds
amount = int(input("Enter amount to withdraw (in hundreds): ")) * 100

# Number of 100, 50, and 10 notes
notes_100 = amount // 100
remaining = amount % 100

notes_50 = remaining // 50
remaining = remaining % 50

notes_10 = remaining // 10
remaining = remaining % 10

print("100s:", notes_100)
print("50s:", notes_50)
print("10s:", notes_10)
if remaining > 0:
    print("Remaining amount that cannot be given in these denominations:", remaining)
