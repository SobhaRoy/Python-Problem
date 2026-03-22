# Input length and breadth
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

# Calculate area and perimeter
area = length * breadth
perimeter = 2 * (length + breadth)

# Compare
if area > perimeter:
    print("Area is greater than perimeter.")
else:
    print("Perimeter is greater than or equal to area.")
