# Number guessing game python using Random Module
import random
Cnumber = random.randrange(1,101)
userInput = int(input("Enter your number:"))

if userInput > Cnumber:
    print("Computer Number",Cnumber)
    print("Your guess number is too high")
elif Cnumber > userInput:
    print("Computer Number",Cnumber)
    print("Your guess number is too low")
else:
    print("Computer Number",Cnumber)
    print("Your guess number is equal")

