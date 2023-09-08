#rock-paper-scissors game developed using RANDOM build-in module

import random
lt = ["rock","paper","scissors"]
i = random.choice(lt)
j = input("Choose rock/paper/scissors: ")
print("Opponent choose : ",i)
print("You choose : ",j)
if i == j:
    print("It is tie.")
elif i == "rock":
    if j == "scissors":
        print("Opponent won the game.")
    elif j == "paper":
        print("Congratulation!! You won the game.")
elif i == "paper":
    if j == "rock":
        print("Opponent won the game.")
    elif j == "scissors":
        print("Congratulation!! You won the game.")
elif i == "scissors":
    if j == "paper":
        print("Opponent won the game.")
    elif j == "rock":
        print("Congratulation!! You won the game.")