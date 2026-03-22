numbers = list(map(int, input("Enter 8 integers: ").split()))

block_count = 0
current_length = 1
longest = 1

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        current_length += 1
    else:
        block_count += 1
        longest = max(longest, current_length)
        current_length = 1

# Handle the last block
block_count += 1
longest = max(longest, current_length)

print("Number of increasing blocks:", block_count)
print("Length of the longest block:", longest)
