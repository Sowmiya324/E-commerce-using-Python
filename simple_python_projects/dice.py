#dice simulator using random package
import random
print("\t\tDice simulator")
print("\t\t--------------")
x=input("\nDo you want to roll the dice?")
while x.lower()!="no":
    a=random.randint(1,6)
    b=random.randint(1,6)
    print("Dice 1:",a)
    print("Dice 2:",b)
    x=input("Do you want to roll the dice again?")
print("Thank you for visiting")
