import random

'''Snake = 1, Water = -1, Gun = 0'''

computer = random.choice([-1,0,1])

youstr= input("Choose any :")
youDict = {"s": 1, "w": -1, "g": 0}
youNum = youDict[youstr]
reverseDict = {1 : "snake", -1 : "water", 0 : "gun"}

print(f"You chose {reverseDict[youNum]} \nComputer Chose {reverseDict[computer]}")

if(computer == youNum):
    print("Game is draw!")
else:
    if(computer == 0 and youNum ==1):
        print("You lose")
    elif(computer == 0 and youNum == -1):
        print("You win")
    elif(computer == 1 and youNum == 0):
        print("You lose")
    elif(computer == 1 and youNum == 0):
        print("You Win")
    elif(computer == 1 and youNum == -1):
        print("You lose")
    else:
        print("Something Went wrong")