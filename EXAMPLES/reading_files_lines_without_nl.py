FILE_PATH = '../DATA/mary.txt'

with open(FILE_PATH) as mary_in:
    lines_without_nl = mary_in.read().splitlines()  # splitlines() splits string on '\n' into lines
    print(lines_without_nl)

with open('../DATA/breakfast.txt') as breakfast_in:
    all_lines = breakfast_in.read().splitlines()
print(f"{all_lines = }\n")

all_foods_no_spam = [food for food in all_lines if food != 'spam']
print(f"{all_foods_no_spam = }\n")
