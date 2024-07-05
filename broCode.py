import random

while True:

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, scissors :").lower()

    if computer == "rock":
        if player == "rock":
            print("Computer : " + computer)
            print("Player : " + player)
            print("Draw :|")
        elif player == "paper":
            print("Computer : " + computer)
            print("Player : " + player)
            print("Win :)")
        else:
            print("Computer : " + computer)
            print("Player : " + player)
            print("Lose :(")

    elif computer == "paper":
        if player == "rock":
            print("Computer : " + computer)
            print("Player : " + player)
            print("Lose :(")
        elif player == "paper":
            print("Computer : " + computer)
            print("Player : " + player)
            print("Draw :|")
        else:
            print("Computer : " + computer)
            print("Player : " + player)
            print("Win :)")
    else:
        if player == "rock":
            print("Computer : " + computer)
            print("Player : " + player)
            print("Win :)")
        elif player == "paper":
            print("Computer : " + computer)
            print("Player : " + player)
            print("Lose :(")
        else:
            print("Computer : " + computer)
            print("Player : " + player)
            print("Draw :|")
    play_again = input("Play again?")
    if play_again != "yes":
        break
print("Bye!")
