matchsticks = 21

while matchsticks > 1:
    user = int(input("Pick 1-4 matchsticks: "))
    
    if user < 1 or user > 4:
        print("Invalid move")
        continue
    
    comp = 5 - user
    matchsticks -= (user + comp)
    
    print("Computer picks:", comp)
    print("Remaining matchsticks:", matchsticks)

print("You are forced to pick the last matchstick. You lose!")
