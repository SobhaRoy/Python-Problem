# Input marks for 5 subjects
marks = []
for i in range(1, 6):
    m = int(input(f"Enter marks for subject {i}: "))
    marks.append(m)

# Calculate aggregate and percentage
aggregate = sum(marks)
percentage = (aggregate / 500) * 100

print("Aggregate Marks:", aggregate)
print("Percentage:", percentage, "%")
