import random
logo = """
  ________                              ___________.__                                 ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____     ____  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/       \/            \/    \/     \/     
"""
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a Number between 1 and 100.")

def random_number():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
             29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 39, 50, 51, 52, 53, 54, 55,
             56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82,
             83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100
             ]
    number = random.choice(numbers)
    return number

def compare_numbers(user_number, pc_number):
    if user_number == pc_number:
        return f"You got it! The answer was {pc_number}"
    elif user_number > pc_number:
        return "Too High.\nGuess again"
    elif user_number < pc_number:
        return "Too Low.\nGuess again."


def play_game():

    computer_number = random_number()
    game_finished = False
    counter = 0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        counter = 10
    elif difficulty == "hard":
        counter = 5
    else:
        print("Not a valid input. Try again")
        play_game()

    while not game_finished:
        user_guess = int(input("Make a guess: "))
        compare_numbers(user_guess,computer_number)
        print(compare_numbers(user_guess,computer_number))

        if compare_numbers(user_guess,computer_number).startswith(f"You got") != True:
            counter -= 1
            print(f"You have {counter} attempts remaining to guess the number")
            if counter == 0:
                print("You' ve run out of guesses, you lose")
                game_finished = True

        else:
            game_finished = True
            while input("Do you want to play again ? Type 'y' or 'n': ").lower() == "y":
                play_game()

play_game()