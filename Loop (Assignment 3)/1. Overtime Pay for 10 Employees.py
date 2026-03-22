for i in range(1, 11):
    hours = int(input(f"Enter hours worked by employee {i}: "))
    
    if hours > 40:
        overtime = (hours - 40) * 12
    else:
        overtime = 0
    
    print(f"Overtime pay for employee {i}: Rs. {overtime}")
