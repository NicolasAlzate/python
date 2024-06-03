from coffeeData import MENU
from coffeeData import resources


def is_sufficient(selection):
    is_enough = True
    for item in selection:
       if selection[item] >= resources[item]:
        print(f"Sorry there is not enough {item}")
        is_enough = False
    return is_enough

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many quarters?: ")) * 0.1
    total += int(input("how many quarters?: ")) * 0.05
    total += int(input("how many quarters?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} in change.")
        global Money
        Money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

is_on = True
while is_on:
    Money = 0
    user_wants = input("What Would You like ? (espresso/latte/cappuccino): ")
    if user_wants == 'off':
        is_on = False
    elif user_wants == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: ${Money}")
    else:
        drink = MENU[user_wants]
        if is_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_wants, drink["ingredients"])




