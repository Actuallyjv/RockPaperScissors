from random import randint

Player = input("Rock, Paper, or Scissors? ")

Options = ["Rock", "Paper", "Scissors"]
ComputerPlay = Options[randint(0, 2)]

if Player == ComputerPlay:
    print("Tie!")
elif Player == "Rock":  # Player chooses Rock
    if ComputerPlay == "Paper":
        print("You lose!", ComputerPlay, "covers", Player)
    else:
        print("You win!", Player, "smashes", ComputerPlay)
elif Player == "Paper":  # Player chooses Paper
    if ComputerPlay == "Scissors":
        print("You lose!", ComputerPlay, "cut", Player)
    else:
        print("You win!", Player, "covers", ComputerPlay)
elif Player == "Scissors":  # Player chooses Scissors
    if ComputerPlay == "Rock":
        print("You lose!", ComputerPlay, "smashes", Player)
    else:
        print("You win!", Player, "cut", ComputerPlay)
else:
    print("Invalid input! Try again.Input must be Rock, Paper, or Scissors.")
