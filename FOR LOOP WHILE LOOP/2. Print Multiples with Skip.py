# Input
n, k = map(int, input("Enter n and k: ").split())
numbers = list(map(int, input(f"Enter {n} integers: ").split()))

first_multiple_skipped = False
for num in numbers:
    if num % k == 0:
        if not first_multiple_skipped:
            first_multiple_skipped = True
        else:
            print(num, end=' ')
print()  # newline
