names = ["Ben","Nicolas","Denice","Negri"]
# names_string contains the input values provided.
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random

random_num = random.randint(0, len(names) - 1)
print(f"{names[random_num]} is going to buy the meal today!")