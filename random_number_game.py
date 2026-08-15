import random

play_again = True
while play_again == True:
    random_number = random.randint(1, 10)
    life_counter = 5
    print(f"You have {life_counter} lives ")
    guessed_number = int(input("Enter a random value from 1-10 "))
    count = 1
    if guessed_number == random_number:
        print(
            f"Your guess was correct and you guessed it in {count} number of gusses without any lives lost"
        )
        break

    else:
        while guessed_number != random_number and life_counter != 0:
            life_counter = life_counter - 1
            count = count + 1
            print(f"You lost a life, you have {life_counter} lives left")
            guessed_number = int(input("Enter a random value from 1-10 "))

    if life_counter > 0:
        print(
            f"Your guess was correct and you guessed in {count} number of guesses with {life_counter} lives left "
        )
    else:
        print(f"No lives left you lost the number was {random_number}")
    play_again = input("Do you want to play again (y/n) ").lower()
    if not play_again == "y":
        play_again == False
