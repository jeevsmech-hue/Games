import art
print(art.logo)
import random

attempts = 0


def comp_num():
    print("Welcome to Number Game\n I am thinking of a number between 1 and 100.")

    life = True
    return random.randint(1, 100)


def start_game():
    computer_number = comp_num()
    player_response = input("Press Enter difficulty 'easy' or 'hard' :")

    if player_response == "easy":
        attempts = 10
    else:
        attempts = 5
    player_guess = int(input(f"you have {attempts} attempts left.\n Make a guess : "))
    while player_guess != computer_number:

        if player_guess > computer_number:
            print("You guessed too high")
            attempts -= 1
            player_guess = int(input(f"you have {attempts} attempts left.\n Make a guess : "))

        elif player_guess < computer_number:
            print("You guessed too low")
            attempts -= 1
            player_guess = int(input(f"you have {attempts} attempts left.\n Make a guess : "))

    while player_guess == computer_number:
        print("You got it right")
        restart = input("Do you want to continue? type 'Y' or 'N'").lower()
        if restart == "y":
            start_game()
        else:
            break


start_game()