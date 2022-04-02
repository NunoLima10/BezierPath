


import pygame, sys
from pygame.constants import MOUSEBUTTONDOWN
from Dot import Dot

pygame.init()

WIDTH, HEIGHT = 1000,700
BG_COLOR = (128, 128, 128)
DOT_COLOR=(230,230,230)
FPS = 60
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bezier Curves')

dot = Dot((100,100),DOT_COLOR,10)

def main():
    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    clique=True

        try:
            mouse_position = pygame.mouse.get_pos()
        except:
            pass

        if dot.position_is_in(mouse_position):
            dot.set_color((0,255,0))
            dot.set_position(mouse_position)
        else:
            dot.set_defaut_color()

        screen.fill(BG_COLOR)
        dot.update(screen)
       




        pygame.display.update()
    




if __name__ == "__main__":
    main()    