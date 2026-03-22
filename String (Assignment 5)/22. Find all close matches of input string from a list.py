from difflib import get_close_matches
lst = input("Enter list of strings separated by commas: ").split(',')
inp = input("Enter string to match: ")
matches = get_close_matches(inp, lst)
print("Close matches:", matches)
