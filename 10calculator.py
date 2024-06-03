


#Add

def add (n1,n2):
    return n1 + n2

#substrac

def substract (n1, n2):
    return n1 - n2

#Multiply

def multiply (n1, n2):
    return n1 * n2

#divide

def divide (n1, n2):
    return  n1/n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

num1 = int(input("Whats the first number ? "))
num2 = int(input("Whats the second number ? "))


for symbol in operations:
    print(symbol)


selected_symbol = input("Pick an operation from line above: ")

calculation_function = operations[selected_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {selected_symbol} {num2} = {answer}")

