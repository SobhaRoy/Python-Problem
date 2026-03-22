# Input number of days late
days_late = int(input("Enter number of days book is late: "))

# Calculate fine
if days_late <= 5:
    fine = 0.5 * days_late
    print("Fine is Rs.", fine)
elif days_late <= 10:
    fine = 1 * days_late
    print("Fine is Rs.", fine)
elif days_late <= 30:
    fine = 5 * days_late
    print("Fine is Rs.", fine)
else:
    print("Membership cancelled due to late return.")
