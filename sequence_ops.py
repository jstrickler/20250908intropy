fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

del fruits[5]
del fruits[-1]
del fruits[2:6]
print(f"{fruits = }\n")

for fruit in 'orange', 'guava', 'peach', 'raspberry':
    print(fruit, fruit in fruits)
print()

person = "Richard Nixon"
print(f"{'char' in person = }")


a = [1, 2, 3]
b = [4, 5]
c = a + b
print(f"{c = }")

f = "foo"
b = "bar"
s = f + b
print(f"{s = }")

print('-' * 60)
print("PYTHON! "* 5)
x = '_' * 10
print(f"{x = }")

flags = [True] * 10
print(f"{flags = }")

more_flags = [True, False, None] * 4
print(f"{more_flags = }")
