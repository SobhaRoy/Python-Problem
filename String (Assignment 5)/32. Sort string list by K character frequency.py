lst = input("Enter list of strings separated by commas: ").split(',')
k = input("Enter character to sort by: ")
sorted_lst = sorted(lst, key=lambda x: x.count(k), reverse=True)
print("Sorted list by frequency of", k, ":", sorted_lst)
