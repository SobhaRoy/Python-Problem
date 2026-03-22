def digit_sum(n):
    return sum(int(d) for d in str(n))

count_numbers = 0

while True:
    n = int(input("Enter a positive integer (<=0 to stop): "))
    if n <= 0:
        break

    count_numbers += 1
    iterations = 0
    result = n
    while result > 9:
        result = digit_sum(result)
        iterations += 1

    print(f"Iterations: {iterations}, Final digit: {result}")

print("Total numbers processed:", count_numbers)
