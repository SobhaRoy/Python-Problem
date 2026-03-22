dic1 = {1:10, 2:20, 4:6}
dic2 = {3:30, 4:40, 5:2}
dic3 = {5:50, 6:60}

result = {}

for d in (dic1, dic2, dic3):
    for key, value in d.items():
        result[key] = result.get(key, 0) + value

print(result)
