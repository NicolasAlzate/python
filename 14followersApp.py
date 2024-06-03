import random
from followersData import data

logo = """
    __  ___       __            
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/    
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/    
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)
"""

print(logo)

celebrity_A = []
celebrity_B = []

def select_celebrity():

    famous = random.choice(data)
    celebrity_A.append(famous)
    followers = celebrity_A[0]['follower_count']
    print(f"Compare A: {celebrity_A[0]['name']}, a {celebrity_A[0]['description']}, from {celebrity_A[0]['country']}. ")
    return followers

def select_celebrity_B():

    famous = random.choice(data)
    celebrity_B.append(famous)
    followers = celebrity_B[0]['follower_count']
    print(f"Against B: {celebrity_B[0]['name']}, a {celebrity_B[0]['description']}, from {celebrity_B[0]['country']}. ")
    return followers


def play_game():

    counter = 0
    game_finished = False

    while not game_finished:
        a = select_celebrity()
        print(vs)
        b = select_celebrity_B()

        answer = input("Who has more followers ? Type 'A' or 'B': ").lower()
        if answer == 'a' and a > b:
            counter += 1
            print(f"You're right! Current Score: {counter}")
            a = b
            b = select_celebrity_B()
        elif answer == 'b' and b > a:
            counter += 1
            print(f"You're right! Current Score: {counter}")
            a = b
            b = select_celebrity_B()
        else:
            print(f"Sorry, that's wrong. Final Score: {counter}")
            game_finished = True
            play_game()

play_game()