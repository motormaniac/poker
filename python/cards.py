import sys
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
