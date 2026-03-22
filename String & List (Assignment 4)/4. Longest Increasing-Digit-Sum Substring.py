def digit_sum(n):
    return sum(int(d) for d in str(n))

numbers = input("Enter numbers separated by spaces: ").split()
digit_sums = [digit_sum(int(num)) for num in numbers]

# Find longest increasing contiguous subsequence
max_len = 1
cur_len = 1
start_index = 0
max_start = 0

for i in range(1, len(digit_sums)):
    if digit_sums[i] > digit_sums[i-1]:
        cur_len += 1
    else:
        if cur_len > max_len:
            max_len = cur_len
            max_start = start_index
        cur_len = 1
        start_index = i

# Check at end
if cur_len > max_len:
    max_len = cur_len
    max_start = start_index

longest_subseq = numbers[max_start:max_start+max_len]
print("Longest increasing digit-sum substring:", longest_subseq)
print("Length:", max_len)
