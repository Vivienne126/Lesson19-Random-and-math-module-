import random
playing=True
number=random.randint(0,10)
while playing:
    guess=int(input("Enter yourguess"))
    if number==guess:
        print("You won the game")
        print("The number is:" , number)
        break
    else:
        print("Your guess is not valid")