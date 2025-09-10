x = 5
y = "cheese"

def my_silly_add(a, b):
    result = a + b
    return result

try:
    result = my_silly_add(x, y)
except (TypeError, ValueError) as err:
    print(err)  # log the error???
except Exception as err:
    print("UNEXPECTED:", err)
else: # no errors
    print(f"{result = }")

print("some more code here...")