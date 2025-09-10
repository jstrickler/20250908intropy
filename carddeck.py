import random
from card import Card

class CardDeck:
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    SUITS = "Clubs Diamonds Hearts Spades".split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):  # "private"
        self._cards = []  # list to hold the 52 cards
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name}:{len(self._cards)}"
    
    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}()"

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    d1.shuffle()
    d2.shuffle()
    print(d1.cards)  # not d1.cards()
    for _ in range(5):
        card = d1.draw()
        print(card)
    print()
    print(d1)
    print(f"{d1 = }")
