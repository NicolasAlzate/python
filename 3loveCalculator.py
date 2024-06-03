print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

true_count = t+r+u+e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

love_count = l+o+v+e

total_score = str(true_count) + str(love_count)

Score = int(total_score)

if (Score < 10) or (Score > 90):
    print(f"Your score is {Score}, you go together like coke and mentos.")
elif (Score >= 40) and (Score <= 50):
    print(f"Your score is {Score}, you are alright together.")
else:
    print(f"Your score is {Score}.")
