colors = []   #  colors = list()
cities = []
dog_breeds = ['English Shepherd', 'German Shepherd', 'Basenji',
              'Beagle', 'Cocker Spaniel']

colors.append('yellow')
cities.append('Sofia')

# instance = CLASS()

# CardDeck MetApiConnection
#  PizzaHelper   TwitchAPI

class Dog:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def bark(self):
        print("woof! woof!")

d1 = Dog("Nellie")
d2 = Dog("Andy")
d1.bark()  # method call
d2.bark()
print(d1.name)
print(d2.name)

class Knight:
    def __init__(self, knight_name):
        pass

    # properties, ...

k = Knight('Arthur')   # read DATA/knights.txt and find 'Arthur'