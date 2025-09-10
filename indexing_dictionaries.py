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

print(f"{airports['SJU'] = }")
print(f"{airports['SJC'] = }")

CODE = 'CVG'
# print(f"{airports['XXM'] = }")
print(f"{CODE in airports = }")
print(f"{airports.get('RDU') = }")
print(f"{airports.get(CODE) = }")
print(f"{airports.get(CODE, 'NOT FOUND') = }")

print(f"{airports.setdefault(CODE, 'Cincinnati') = }")
print(f"{airports = }\n")

for code, city in airports.items():
    print(code, city)
print('-' * 60)

for code, city in sorted(airports.items()):
    print(code, city)
print('-' * 60)

for code in airports:
    print(code)
print('-' * 60)

for city in airports.values():
    print(city)
print('-' * 60)


