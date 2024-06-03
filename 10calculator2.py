


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
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from line above: ")
num2 = int(input("Whats the second number ? "))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("Whats the next number ? "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(answer, num3)

print(f"{answer} {operation_symbol} {num3} = {second_answer}")