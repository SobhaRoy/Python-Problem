# Input details
health = input("Enter health (excellent/poor): ").lower()
age = int(input("Enter age: "))
location = input("Enter location (city/village): ").lower()
sex = input("Enter sex (male/female): ").lower()

# Initialize
insured = False
premium_rate = 0
max_amount = 0

# Check conditions
if health == "excellent" and 25 <= age <= 35 and location == "city":
    if sex == "male":
        insured = True
        premium_rate = 4
        max_amount = 200000
    elif sex == "female":
        insured = True
        premium_rate = 3
        max_amount = 100000
elif health == "poor" and 25 <= age <= 35 and location == "village" and sex == "male":
    insured = True
    premium_rate = 6
    max_amount = 10000

# Output
if insured:
    print(f"Person is insured. Premium rate: Rs.{premium_rate} per thousand. Max amount: Rs.{max_amount}")
else:
    print("Person is not insured.")
