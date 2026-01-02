import sys
import random
sys.path.append(".")
from python.constants import *
from python.spritesheet import SpriteSheet

card_spritesheet = SpriteSheet(
    "assets/playing_card_spritesheet.png",
    grid_size=(13, 5),
    tile_size=(79, 109),
    margin=(1, 1),
    offset=(1, 1)
)

CARD_IMGS = []
for col in range(13):
    for row in range(4):  # Only 4 rows for suits
        image = card_spritesheet.get_image(col, row)
        CARD_IMGS.append(image)
CARD_BACK_IMG = card_spritesheet.get_image(0, 4)

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __repr__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    suits = ["H", "D", "C", "S"] #hearts diamonds clubs spades
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = []
        for suit in self.suits:  #iterating through suits and ranks
            for rank in self.ranks:
                self.cards.append(Card(suit, rank)) #add new card to deck
            random.shuffle(self.cards) #randomizing card order
    def deal(self):
            return self.cards.pop()   #takes last card out and returns it