def interleaved_merge(s1, s2):
    result = []
    len1, len2 = len(s1), len(s2)
    for i in range(max(len1, len2)):
        if i < len1:
            result.append(s1[i])
        if i < len2:
            result.append(s2[-(i+1)])  # take from end of s2
    # Append leftover characters if any
    if len1 > len2:
        result.extend(s1[len2:])
    elif len2 > len1:
        result.extend(reversed(s2[:len2-len1]))
    return ''.join(result)

# Example usage
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
merged = interleaved_merge(s1, s2)
print("Interleaved merged string:", merged)
