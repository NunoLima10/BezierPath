


import pygame, sys

from Dot_class import Dot
from dots_suporte import dots_update, draw_quadratic_bezierlines, mouse_clik,draw_cubic_bezierlines

pygame.init()

WIDTH, HEIGHT = 1000,700
BG_COLOR = (128, 128, 128)
DOT_COLOR=(230,230,230)
FPS = 60
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bezier Curves')


def main():
    dots_quadratic_bezier = {
        "P0":Dot((200,250),DOT_COLOR,10),
        "P1":Dot((400,100),DOT_COLOR,5),
        "P2":Dot((600,250),DOT_COLOR,10)
    }

    dots_cubic_bezier = {
        "P0":Dot((200,450),DOT_COLOR,10),
        "P1":Dot((400,300),DOT_COLOR,5),
        "P2":Dot((600,450),DOT_COLOR,5),
        "P3":Dot((600,550),DOT_COLOR,10)

    }

    

    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()

            mouse_clik(event,dots_quadratic_bezier,pygame.mouse.get_pos())
            mouse_clik(event,dots_cubic_bezier,pygame.mouse.get_pos())
            
        try:
            mouse_position = pygame.mouse.get_pos()
        except:
            pass

        screen.fill(BG_COLOR)
        draw_quadratic_bezierlines(dots_quadratic_bezier, screen)
        dots_quadratic_bezier = dots_update(dots_quadratic_bezier, screen, mouse_position)

        draw_cubic_bezierlines(dots_cubic_bezier, screen)
        dots_cubic_bezier = dots_update(dots_cubic_bezier, screen, mouse_position)

    
    
        pygame.display.update()
      
    




if __name__ == "__main__":
    main()    