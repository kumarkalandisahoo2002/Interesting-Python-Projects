#Color prediction game using RANDOM build-in module
import random
lt = ["red","green","perpule"]
i = random.choice(lt)
j = input("Predict a color(red/green): ")
print("Output:",i)
print("You predict:",j)

if i == j:
    print("Congratulation!! Your prediction is correct.")
elif i == "perpule":
    print("Your prediction is partially correct.")
elif i != j:
    print("sorry!! Your prediction is wrong.")


