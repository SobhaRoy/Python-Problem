strings = input("Enter list of strings separated by commas: ").split(',')
char = input("Enter character to count: ")
freq_list = [s.count(char) for s in strings]
print("Frequency in each string:", freq_list)
