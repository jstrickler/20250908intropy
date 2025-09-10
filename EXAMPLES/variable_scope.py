ANIMAL = "wombat"  # global variable

class Dog:
    pass

def spam():
    a = 100   # local variable
    print(f"{ANIMAL = }")
    print(f"{a = }")

def ham():
    a = "apple"  # local variable
    print(f"{ANIMAL = }")
    print(f"{a = }")

def eggs(color):
    # color is local variable
    print(f"{ANIMAL = }")
    print(f"{color = }")

spam()
print()  # blank line
ham()
print()
eggs("green")