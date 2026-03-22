s = input("Enter string: ").lower()
vowels = set('aeiou')
if vowels.issubset(set(s)):
    print("Contains all vowels")
else:
    print("Does not contain all vowels")
