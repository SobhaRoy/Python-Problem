d1 = {'key1': 1, 'key2': 3, 'key3': 2}
d2 = {'key1': 1, 'key2': 2}

for key in d1:
    if key in d2 and d1[key] == d2[key]:
        print(f"{key}: {d1[key]} is present in both")
