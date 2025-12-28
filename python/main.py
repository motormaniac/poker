import pygame
import sys
sys.path.append(".")

# some things in other files require pygame to be initialized first
pygame.init()
from python.constants import *
WIN = pygame.display.set_mode((WORLD_CONSTANTS.WIDTH, WORLD_CONSTANTS.HEIGHT))
from python.cards import CARD_IMGS, CARD_BACK_IMG
pygame.display.set_caption("game")

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)  # 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False
        WIN.fill((0, 100, 0))
        WIN.blit(CARD_BACK_IMG, (100, 100))  # Draw Ace of Spades
        WIN.blit(CARD_IMGS[0], (150, 100))  # Draw Ace of Hearts
        WIN.blit(CARD_IMGS[1], (200, 100))  # Draw Ace of Hearts
        pygame.display.update()


if __name__ == "__main__":
    main()