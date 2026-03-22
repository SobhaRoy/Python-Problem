def sliding_window_stats(nums, k):
    from statistics import mean, pstdev
    result = []
    for i in range(len(nums) - k + 1):
        window = nums[i:i+k]
        avg = mean(window)
        var = pstdev(window) ** 2  # variance from standard deviation
        result.append((avg, var))
    return result

# Example usage
nums = list(map(float, input("Enter list of numbers: ").split()))
k = int(input("Enter window size: "))

stats = sliding_window_stats(nums, k)
print("Sliding window (avg, variance):")
for t in stats:
    print(t)
