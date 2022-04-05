
import pygame, sys
from bezier_cuve import BezierCuve
from radioButton import RadioButton
from slider import Slider

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

    radio_button = RadioButton((30,30), (255,255,255), 12, "Guidelines")
    slider_t = Slider((18,60), (200,10), (255,255,255) ,1, "t =")
    slider_q = Slider((18,120), (200,10), (255,255,255), 0.05, "Q =")

    bezier_cuve2 = BezierCuve(2, DOT_COLOR, (255,255,255))
    bezier_cuve3 = BezierCuve(3, DOT_COLOR, (255,255,255))

    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()

            mouse_position = pygame.mouse.get_pos()

            radio_button.mouse_trigger(event)
            slider_t.mouse_trigger(event)
            slider_q.mouse_trigger(event)        
            bezier_cuve2.mouse_trigger(event)
            bezier_cuve3.mouse_trigger(event)

        mouse_position = pygame.mouse.get_pos()
        screen.fill(BG_COLOR)

        radio_button.update(screen,mouse_position)
        show_guidelines = radio_button.get_state()

        slider_t.update(screen,mouse_position)
        t_max = slider_t.get_swiper_percentage()


        slider_q.update(screen,mouse_position)
        Q = slider_q.get_swiper_percentage() 
        
       
        bezier_cuve2.update(screen,mouse_position,t_max,Q,show_guidelines)
        bezier_cuve3.update(screen,mouse_position,t_max,Q,show_guidelines)

        pygame.display.update()


if __name__ == "__main__":
    main()    