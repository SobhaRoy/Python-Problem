s = input("Enter string: ")
words = s.split()
even_words = [w for w in words if len(w) % 2 == 0]
print("Even length words:", even_words)
