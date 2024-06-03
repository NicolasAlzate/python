def my_function():
    print("This is your function")

my_function()

def greet_with_name(name):
    print(f"Hello {name}")

greet_with_name("Nicolas")

def greet_with_name(name,Location):
    print(f"Hello {name}, do you live in {Location} ?")

greet_with_name(Location="Bogota", name="Nicolas")
greet_with_name("Nicolas", "Bogota")