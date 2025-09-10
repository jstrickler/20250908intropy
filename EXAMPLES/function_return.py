def get_hello():
    return "Hello, world"

h = get_hello() 
print(f"{h = }")

get_hello() # ignores function return value

def hello():
    print("Hello, world")

h = hello()
print(f"{h = }")

def double(x):
    return x * 2

d = double(10)
print(f"{d = }")

print(f"{double(500) = }")

def make_repeat(s, count=1):
    return s * count

a = make_repeat('-', 50)
print(f"{a = }")

a = make_repeat('-')
print(f"{a = }")

print(f"{double('beep') = }")

