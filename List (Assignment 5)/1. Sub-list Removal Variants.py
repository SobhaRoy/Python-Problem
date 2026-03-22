def sublist_removals(lst):
    result = []
    for i in range(len(lst)):
        new_list = lst[:i] + lst[i+1:]
        result.append(new_list)
    return result

# Example usage
lst = list(map(int, input("Enter list of integers: ").split()))
all_variants = sublist_removals(lst)
print("All sub-lists after removing one element:")
for variant in all_variants:
    print(variant)
