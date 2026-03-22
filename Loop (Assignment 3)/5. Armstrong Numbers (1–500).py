for num in range(1, 501):
    temp = num
    sum = 0
    
    while temp > 0:
        digit = temp % 10
        sum += digit**3
        temp //= 10
    
    if sum == num:
        print(num)
