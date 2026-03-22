s = input("Enter string: ")
words = s.split()
new_words = []
for w in words:
    if len(w) > 1:
        new_words.append(w[0].upper() + w[1:-1] + w[-1].upper())
    else:
        new_words.append(w.upper())
print("Result:", " ".join(new_words))
