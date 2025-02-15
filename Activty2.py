import random
while True:
    user=input("Enter your choice ")
    actions=["Rock" , "Paper" , "Sisors"]
    computer=random.choice(actions)
    if user==computer:
        print("You have a tie")
    elif user=="Rock":
        if computer=="Paper":
            print("You win")
        else:
            print("You loose")
    elif user=="Paper":
        if computer=="Sisors":
            print("You win")
        else:
            print("You loose")
    elif user=="Sisors":
        if computer=="Rock":
            print("You win")
        else:
            print("You loose")