s = input("Enter string: ")
word = input("Enter word to find: ")
index = s.find(word)
if index != -1:
    print(f"Word found at index: {index}")
else:
    print("Word not found")
