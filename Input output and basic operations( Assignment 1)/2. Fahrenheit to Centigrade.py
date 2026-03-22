# Input temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert to Centigrade
centigrade = (fahrenheit - 32) * 5/9

print("Temperature in Centigrade:", round(centigrade, 2), "°C")
