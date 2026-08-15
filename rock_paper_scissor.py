import random

options = ("rock","paper","scissor")
running = True

while running:
     player = None
     computer = random.choice(options)

     while player not in options:
        player = input("Enter a choice: ROCK or PAPER or Scissors\n").lower()

     print(f"Player: {player}")
     print(f"Computer: {computer}")

     if player == computer:
        print("Its a tie.")
     elif (
        (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
        or (player == "rock" and computer == "scissors")
    ):
        print("You win")
     else:
        print("You loose")

     if not input("Play again? (y/n): ").lower() == "y":
        running = False