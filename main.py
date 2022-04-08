
import pygame, sys
from bezier_cuve import BezierCuve
from radioButton import RadioButton
from slider import Slider
from bezier_path import BezierPath


pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1080,720
BG_COLOR = (128, 128, 128)
DOT_COLOR=(230,230,230)
FPS = 60
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bezier Curves')



def main():

    radio_button = RadioButton((30,30), (255,255,255), 12, "Guidelines")
    radio_button2 = RadioButton((30,70), (255,255,255), 12, "Dots")

    slider_t = Slider((18,100), (200,10), (255,255,255) ,1, "t =")
    slider_q = Slider((18,130), (200,10), (255,255,255), 0.05, "Q =")

    bezier_path = BezierPath(DOT_COLOR, DOT_COLOR)
    Ctrl_key_state = False
    show_guidelines = False


    #bezier_cuve2 = BezierCuve(2, DOT_COLOR, (255,255,255))
    #bezier_cuve3 = BezierCuve(3, DOT_COLOR, (255,255,255))

    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN and pygame.K_LCTRL: 
                Ctrl_key_state = True 

            if event.type == pygame.KEYUP and event.key == pygame.K_LCTRL:
                Ctrl_key_state = False

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if Ctrl_key_state:
                     mouse_position = pygame.mouse.get_pos()
                     bezier_path.add_dot(mouse_position)

            radio_button.mouse_trigger(event)
            radio_button2.mouse_trigger(event)
            slider_t.mouse_trigger(event)
            slider_q.mouse_trigger(event)
            bezier_path.mouse_trigger(event)

            #bezier_cuve2.mouse_trigger(event)
            #bezier_cuve3.mouse_trigger(event)

        mouse_position = pygame.mouse.get_pos()
        screen.fill(BG_COLOR)

        radio_button.update(screen,mouse_position)
        show_guidelines = radio_button.get_state()

        radio_button2.update(screen,mouse_position)
        show_dots = radio_button2.get_state()

        slider_t.update(screen,mouse_position)
        t_max = slider_t.get_swiper_percentage()


        slider_q.update(screen,mouse_position)
        Q = slider_q.get_swiper_percentage() 
        Q = 0.01 if Q <=0 else Q 
        
        bezier_path.update(screen, mouse_position, t_max, Q, show_guidelines,show_dots)


        #bezier_cuve2.update(screen,mouse_position,t_max,Q,show_guidelines)
        #bezier_cuve3.update(screen,mouse_position,t_max,Q,show_guidelines)

        pygame.display.update()


if __name__ == "__main__":
    main()    