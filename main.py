


import pygame, sys

from Dot_class import Dot
from dots_suporte import dots_update, draw_dots_lines, mouse_clik

pygame.init()

WIDTH, HEIGHT = 1000,700
BG_COLOR = (128, 128, 128)
DOT_COLOR=(230,230,230)
FPS = 60
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bezier Curves')


def main():
    dots ={
        "P0":Dot((200,350),DOT_COLOR,10),
        "P1":Dot((400,200),DOT_COLOR,5),
        "P2":Dot((600,350),DOT_COLOR,10)
    }
    

    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()

            mouse_clik(event,dots,pygame.mouse.get_pos())
            
        try:
            mouse_position = pygame.mouse.get_pos()
        except:
            pass

        screen.fill(BG_COLOR)
        draw_dots_lines(dots, screen)
        dots = dots_update(dots, screen, mouse_position)
    
    
        pygame.display.update()
      
    




if __name__ == "__main__":
    main()    