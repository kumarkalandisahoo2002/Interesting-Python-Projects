#number(digit) prediction using RANDOM build-in module
import random
i = random.randint(0,9)
j = int(input("Predict a number(digit): "))
print("Output:",i)
print("You predict:",j)

if i == j:
    print("Congratulation!! Your prediction is correct.")
else:
    print("Sorry!! your prection is not correct.")