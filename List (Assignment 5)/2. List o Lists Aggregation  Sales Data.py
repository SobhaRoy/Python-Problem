sales = [
    [5, 3, 0, 2],
    [7, 0, 2, 1],
    [0, 1, 4, 0]
]

# Compute total sales per product
num_products = len(sales[0])
total_sales = [sum(day[i] for day in sales) for i in range(num_products)]

max_sales = max(total_sales)
min_sales = min(total_sales)
max_products = [i+1 for i, val in enumerate(total_sales) if val == max_sales]
min_products = [i+1 for i, val in enumerate(total_sales) if val == min_sales]

# Print summary
for i, total in enumerate(total_sales):
    print(f"Product {i+1}: Total Sales = {total}")

print("Product(s) with maximum sales:", max_products)
print("Product(s) with minimum sales:", min_products)
