# Input basic salary
basic_salary = float(input("Enter basic salary: "))

# Calculate allowances
da = 0.4 * basic_salary
hra = 0.2 * basic_salary

# Calculate gross salary
gross_salary = basic_salary + da + hra

print("Gross Salary:", gross_salary)
