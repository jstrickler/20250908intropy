fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

f1 = sorted(fruits)
print(f"{f1 = }\n")

#                  key=FUNCTION OBJECT  (not FUNCTION CALL)
f2 = sorted(fruits, key=str.upper)
print(f"{f2 = }\n")

f3 = sorted(fruits, key=len)
print(f"{f3 = }\n")

def wombat(fruit):
    return len(fruit), fruit.lower()

f4 = sorted(fruits, key=wombat)
print(f"{f4 = }\n")

def wacky(one_item):
    comparison_value = one_item[-1].lower()
    print(f"Comparing {one_item} as {comparison_value}")
    return comparison_value

f5 = sorted(fruits, key=wacky)
print(f"{f5 = }\n")

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

n1 = sorted(nums)
print(f"{n1 = }\n")

n2 = sorted(nums, key=str)
print(f"{n2 = }\n")

def wacky(f):
    return f[-1].lower()

# inline, anonymous function
f5 = sorted(fruits, key=lambda f: f[-1].lower())
print(f"{f5 = }\n")

# don't do that
# x = lambda m: 2 * m   BAD PRACTICE

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_dob(person_tuple):
    return person_tuple[-1]

for person in sorted(people, key=by_dob):
    print(person)
print()
print('-' * 60)
for person in sorted(people, key=lambda p: (p[1], p[0])):
    print(person)
print()

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}
print(f"{airports.items() = }\n")

for code, city in sorted(airports.items()):
    print(code, city)
print('-' * 60)

def by_value(item):
    return item[1], item[0]

for code, city in sorted(airports.items(), key=by_value):
    print(code, city)
print('-' * 60)

print(f"{nums = }\n")
nums.sort()
print(f"{nums = }\n")

f6 = sorted(fruits, key=str.lower, reverse=True)
print(f"{f6 = }\n")
