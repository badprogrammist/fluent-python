import collections
from random import choice
from math import hypot

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = dict(spades=3, hearts=2, diamonds=1, clubs=0)


    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits.keys()
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]

    @staticmethod
    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(FrenchDeck.suits) + FrenchDeck.suits[card.suit]

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


def check_deck():
    deck = FrenchDeck()

    assert len(deck) == 52

    assert deck[5].rank == '7'
    assert deck[5].suit == 'spades'

    print('random:', choice(deck))
    print('first 3 cards:', deck[:3])
    print('skip 13 cards:', deck[12::13])

    for card in deck[:3]:
        print('iteration item:', card)

    assert Card('Q', 'hearts') in deck
    assert Card('7', 'beasts') not in deck

    sorted_deck = sorted(deck, key=FrenchDeck.spades_high)
    assert sorted_deck[0].rank == '2'
    assert sorted_deck[0].suit == 'clubs'
    assert sorted_deck[51].rank == 'A'
    assert sorted_deck[51].suit == 'spades'

def check_vector():
    v1 = Vector(3, 4)
    v2 = Vector(5, 6)
    assert abs(v1) == 5

    v3 = v1 + v2
    assert v3.x == 8 and v3.y == 10

    v4 = v1 * 2
    assert v4.x == 6 and v4.y == 8

if __name__ == '__main__':
    check_deck()
    check_vector()
