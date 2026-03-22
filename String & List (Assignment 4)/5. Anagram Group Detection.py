from collections import defaultdict

words = input("Enter words separated by spaces: ").split()
groups = defaultdict(list)

for word in words:
    key = ''.join(sorted(word))
    groups[key].append(word)

# Convert to list of groups
anagram_groups = list(groups.values())
print("Anagram groups:", anagram_groups)
