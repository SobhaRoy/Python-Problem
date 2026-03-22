d = {
    'x': list(range(11,20)),
    'y': list(range(21,30)),
    'z': list(range(31,40))
}

print(d['x'][4])
print(d['y'][4])
print(d['z'][4])

for key in d:
    print(key, "has value", d[key])
