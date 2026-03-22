def rotate_and_merge(A, B, k):
    n = len(A)
    k %= n  # handle k > n
    rotated_A = A[-k:] + A[:-k]  # right rotation
    result = [rotated_A[i] + B[i] for i in range(n)]
    return result

# Example usage
A = list(map(int, input("Enter list A: ").split()))
B = list(map(int, input("Enter list B: ").split()))
k = int(input("Enter rotation k: "))

merged = rotate_and_merge(A, B, k)
print("Resulting list after rotation and merging:", merged)
