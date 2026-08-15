import random
start_new_game = True
while start_new_game :
    guessed_number = None
    number = random.randint(1, 100)
    guess_counter = 0
    life = 10
    print("You have", life, "lives")
    while guessed_number not in range(1,100):
        guessed_number = int(input(f'Enter a number between (1-100): '))
    if guessed_number < 1 or guessed_number > 100:
        print(f"Number out of range try again")
        continue
    while guessed_number != number and life > 0:

        guess_counter = guess_counter + 1
        life = life - 1
        print(f"Your guess was incorrect with {life} lives left ")

        if guessed_number < number:
            print("Guess Higher")
        else:
            print("Guess Lower")
        guessed_number = int(input(f"Guess a number "))
    if life > 0:
        print(
            f"{guessed_number} was correct, you guessed it in {guess_counter + 1} attempt"
        )
    else:
        print(f"You loose the number was {number}")
    start_new_game = input("Would you like to start a new game (y/n) ").lower()
    if not start_new_game == "y":
        start_new_game = False
