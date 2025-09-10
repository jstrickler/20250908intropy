class Card:  # inherits from 'object'
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"Card:{self.rank}/{self.suit}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card('8', 'Diamonds')  # Card.__init__(new-obj, ...)
    c2 = Card('A', 'Hearts')
    print(c1)   # str(c1)
    print(f"{c1 = }")   # repr(c1)
    
    print(c1.rank, c1.suit)
    