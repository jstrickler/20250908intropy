from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()  # call CardDeck._make_deck()
        for joker_number in 1, 2:
            card = Card(f"Joker-{joker_number}", "*** JOKER ***")
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(f"{j.cards = }")
    print(f"{j = }")
    