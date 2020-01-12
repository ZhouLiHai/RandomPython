import collections
from random import choice

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()

# __len__方法
print(len(deck))

# __getitem__方法
print(deck[0])

# randome.choice方法
print(choice(deck))
print(choice(deck))
print(choice(deck))

# 实现特殊方法可以让你方便的试用Python标准库，不用重新发明轮子
[card for card in deck]
[card for card in reversed(deck)]

# 实现升序排序
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

random_cards = [choice(deck) for _ in range(10)]

for card in sorted(random_cards, key=spades_high):
    print(card)

# python包含大量的内置特殊方法，实现他们可以然你的类像Python风格一样运行
# 给终端记录的__repr__和个用户看的__str__