def longest_peak_subseq(lst):
    max_len = 0
    peak_subseq = None
    
    n = len(lst)
    for i in range(1, n-1):
        # Check for peak
        if lst[i-1] < lst[i] > lst[i+1]:
            # expand left
            left = i-1
            while left > 0 and lst[left-1] < lst[left]:
                left -= 1
            # expand right
            right = i+1
            while right < n-1 and lst[right] > lst[right+1]:
                right += 1
            curr_len = right - left + 1
            if curr_len > max_len:
                max_len = curr_len
                peak_subseq = lst[left:right+1]
                
    if peak_subseq:
        print("Longest increasing-then-decreasing subsequence:", peak_subseq)
        print("Length:", max_len)
    else:
        print("No peak subsequence found")

# Example usage
lst = list(map(int, input("Enter list of integers: ").split()))
longest_peak_subseq(lst)
