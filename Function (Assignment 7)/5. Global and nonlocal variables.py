x = 10  # global variable

def outer():
    y = 5  # nonlocal example
    def inner():
        nonlocal y
        global x
        y += 1
        x += 1
        print("Inner y:", y, "x:", x)
    inner()
    print("Outer y:", y)

outer()
print("Global x:", x)
