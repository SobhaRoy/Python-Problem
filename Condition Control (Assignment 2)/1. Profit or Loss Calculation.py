# Input cost price and selling price
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

# Calculate profit or loss
if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit of Rs.", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("Loss of Rs.", loss)
else:
    print("No profit, no loss.")
