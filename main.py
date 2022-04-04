
import pygame, sys
from bezier_cuve import BezierCuve
from radioButton import RadioButton

from pygame.constants import MOUSEBUTTONDOWN,MOUSEBUTTONUP
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1000,700
BG_COLOR = (128, 128, 128)
DOT_COLOR=(230,230,230)
FPS = 60
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bezier Curves')



def main():

    button = RadioButton((30,30), (255,255,255), 12, "Guidelines")
    bezier_cuve2 = BezierCuve(2, DOT_COLOR, (255,255,255))
    bezier_cuve3 = BezierCuve(3, DOT_COLOR, (255,255,255))

    show_guidelines = True

    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  
                    if button.is_on_focus(pygame.mouse.get_pos()):
                        show_guidelines = False if show_guidelines else True
                        button.set_state(show_guidelines)

            bezier_cuve2.mouse_trigger(event, pygame.mouse.get_pos())
            bezier_cuve3.mouse_trigger(event, pygame.mouse.get_pos())

            
        try:
            mouse_position = pygame.mouse.get_pos()
        except:
            pass

        screen.fill(BG_COLOR)
        button.draw_button(screen)
        button.is_on_focus(pygame.mouse.get_pos())

        bezier_cuve2.update(screen,mouse_position,0.01,show_guidelines)
        bezier_cuve3.update(screen,mouse_position,0.01,show_guidelines)

        

        pygame.display.update()


if __name__ == "__main__":
    main()    