numbers = list(map(int, input("Enter integers: ").split()))

accepted = []
expect_even = True  # start expecting even number

for num in numbers:
    if expect_even and num % 2 == 0:
        accepted.append(num)
        expect_even = False
    elif not expect_even and num % 2 != 0:
        accepted.append(num)
        expect_even = True

print("Accepted sequence:", accepted)
