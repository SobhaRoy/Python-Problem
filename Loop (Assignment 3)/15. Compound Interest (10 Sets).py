for i in range(1, 11):
    print(f"\nSet {i}:")
    p = float(input("Enter principal: "))
    r = float(input("Enter rate (%): ")) / 100
    n = int(input("Enter years: "))
    q = int(input("Enter compounding frequency: "))
    
    a = p * (1 + r/q) ** (n*q)
    
    print("Amount:", a)
