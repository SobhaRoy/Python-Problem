for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            print(i, j, k)



for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            if i != j and j != k and i != k:
                print(i, j, k)
