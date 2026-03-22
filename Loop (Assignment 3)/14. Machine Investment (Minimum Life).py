cost = 6000
salvage = 2000
earning = 1000
rate = 0.12

year = 1

while True:
    total_earning = earning * year
    investment = cost - salvage
    
    alt = cost * ((1 + rate) ** year - 1)
    
    if total_earning >= alt:
        print("Minimum life of machine:", year, "years")
        break
    
    year += 1
