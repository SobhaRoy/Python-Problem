# Input
n = int(input("Enter number of integers: "))
numbers = list(map(int, input(f"Enter {n} integers: ").split()))

sum_even = sum(num for num in numbers if num % 2 == 0)
sum_odd = sum(num for num in numbers if num % 2 != 0)

print("Sum of evens:", sum_even)
print("Sum of odds:", sum_odd)
