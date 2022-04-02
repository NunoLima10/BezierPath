from tkinter import X
import pygame
from pygame.constants import MOUSEBUTTONDOWN,MOUSEBUTTONUP

def mouse_clik(event ,dots, mouse_position) -> None:
    if event.type==MOUSEBUTTONDOWN:
        if event.button==1:
            for dot in dots.values():
                if dot.position_is_in(mouse_position):
                    dot.set_over(True)
        
    if event.type==MOUSEBUTTONUP:
        if event.button==1:
            for dot in dots.values():
                if dot.position_is_in(mouse_position):
                    dot.set_over(False)

def dots_update(dots, surface, mouse_position) -> dict:
     
     for dot in dots.values():
        if dot.position_is_in(mouse_position) and not dot.over:
            dot.set_color((0,255,0))    
        elif dot.over:
            dot.set_color((255,0,0))
            dot.set_position(mouse_position)
        else:
            dot.set_defaut_color() 
        dot.draw(surface)   
     return dots  


def draw_dots_lines(dots, surface) -> None:
    pygame.draw.line(surface,(0,255,0),dots["P0"].position,dots["P1"].position)
    pygame.draw.line(surface,(0,255,0),dots["P2"].position,dots["P1"].position)

    t =0
    t_next=0.01
    while(1 > t_next):
        point1 = quadratic_bezier(dots,t) 
        point2 = quadratic_bezier(dots,t_next)

        pygame.draw.line(surface,(255,255,255),point1,point2)

        t+=0.01
        t_next+=0.01





def quadratic_bezier(dots,t):
    pos_P0 = dots["P0"].position
    pos_P1 = dots["P1"].position
    pos_P2 = dots["P2"].position
    
    x_final = (1 -t) ** 2 * pos_P0[0] + (1 -t) * 2 * t * pos_P1[0] + t * t * pos_P2[0]
    y_final = (1 -t) ** 2 * pos_P0[1] + (1 -t) * 2 * t * pos_P1[1] + t * t * pos_P2[1]

    return [x_final,y_final]
















            


