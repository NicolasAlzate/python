import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

users_option = int(input("What do you chose ? Type O for Rock, 1 for paper or 2 for scissors.\n"))
if users_option == 0:
    print(rock)
elif users_option == 1:
    print(paper)
elif users_option == 2:
    print(scissors)
else:
    print("Type a valid option")
options = [rock, paper, scissors]
random_option = random.randint( 0, len(options) - 1)
print("Computer Chose:")
if random_option == 0:
    print(rock)
elif random_option == 1:
    print(paper)
elif random_option == 2:
    print(scissors)

if users_option == random_option:
    print("Draw")
elif users_option == 0 and random_option == 1:
    print("You Lose")
elif users_option == 0 and random_option == 2:
    print("You Win")
elif users_option == 1 and random_option == 0:
    print("You Win")
elif users_option == 1 and random_option == 2:
    print("You Lose")
elif users_option == 2 and random_option == 0:
    print("You Lose")
elif users_option == 2 and random_option == 1:
    print("You Win")