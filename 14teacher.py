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

def print_format(celebrity):
    name = celebrity["name"]
    description = celebrity["description"]
    country = celebrity["country"]
    return f"{name}, a {description}, from {country}"

def check(answer, a_followers, b_followers):
    if a_followers > b_followers:
        return answer == "a"
    else:
        return answer == "b"


score = 0
game_is_finished = False
famous_b = random.choice(data)

while not game_is_finished:
    famous_a = famous_b
    famous_b = random.choice(data)

    while famous_a == famous_b:
        famous_b = random.choice(data)

    print(f"Compare A: {print_format(famous_a)}")
    print(vs)
    print(f"Against B: {print_format(famous_b)}")

    answer = input("Who has more followers ? Type 'A' or 'B': ").lower()

    count_a = famous_a["follower_count"]
    count_b = famous_b["follower_count"]

    is_correct = check(answer, count_a, count_b)

    if is_correct:
        score += 1
        print(f"You' right, Current Score is: {score}")
    else:
        print(f"Sorry, that's wrong. Final Score is: {score}")
        game_is_finished = True