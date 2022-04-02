

import pygame, sys
from pygame.constants import MOUSEBUTTONDOWN

pygame.init()

WIDTH, HEIGHT = 1000,700
BG_COLOR = (128, 128, 128)
DOT_COLOR=(230,230,230)
FPS = 60
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bezier Curves')


def main():
    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    clique=True
        screen.fill(BG_COLOR)
        pygame.display.update()
    



if __name__ == "__main__":
    main()    