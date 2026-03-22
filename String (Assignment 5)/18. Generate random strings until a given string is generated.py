import random
import string
target = input("Enter target string: ")
attempts = 0
while True:
    rand_str = ''.join(random.choices(string.ascii_letters, k=len(target)))
    attempts += 1
    if rand_str == target:
        break
print("Generated target after attempts:", attempts)
