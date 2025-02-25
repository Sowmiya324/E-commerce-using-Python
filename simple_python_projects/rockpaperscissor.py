import random
print("\t\t\tROCK PAPER SCISSOR")
print("\t\t\t------------------")
print("Lets start the game!!!")
print("Enter your input, if you want to quit the game please enter \'exit\'.")
x=["rock","paper","scissor"]
c_s=0
u_s=0
u=input("\nRock,Paper or Scissor?")
while u.lower()!="exit":
    c=random.choice(x)
    print("Computer:",c)
    if u.lower()==c:
        print("Tie")
    elif u.lower()=="rock":
        if c=="scissor":
            u_s+=1
            print("You win!!")
        else:
            c_s+=1
            print("You loss!!")
    elif u.lower()=="paper":
        if c=="rock":
            u_s+=1
            print("You win!!")
        else:
            c_s+=1
            print("You loss!!")
    elif u.lower()=="scissor":
        if c=="paper":
            u_s+=1
            print("You win!!")
        else:
            c_s+=1
            print("You loss!!")
    else:
        print("Please enter a valid options!!!!")
    u=input("Rock,Paper or Scissor?")
print("\n-------------------------")
print("\tResults")
print("-------------------------")
print("Your score      :",u_s)
print("Computer score  :",c_s)
print("-------------------------")
if u_s>c_s:
    print("Congrats,You win the game!")
elif u_s==c_s:
    print("The game is tie!!!")
else:
    print("You loss the game!!!!")
