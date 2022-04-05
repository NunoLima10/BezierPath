
import pygame
from pygame.constants import MOUSEBUTTONDOWN,MOUSEBUTTONUP
from dot import Dot

class BezierCuve:
    def __init__(self, order:int, dot_color: tuple, line_color:tuple) -> None:
        super().__init__()
        self.order = order
        self.dot_color = dot_color
        self.line_color = line_color

        self.is_quadratic = order == 2

        if self.is_quadratic: 
            self.dots = {
                "P0":Dot((200,300),self.dot_color,8),
                "P1":Dot((300,200),(200,200,200),5),
                "P2":Dot((400,300),self.dot_color,8)
                }
        else: 
            self.dots = {
            "P0":Dot((200,600),self.dot_color,8),
            "P1":Dot((300,500),(200,200,200),5),
            "P2":Dot((600,500), (200,200,200),5),
            "P3":Dot((600,600),self.dot_color,8)
            }

    def mouse_trigger(self, event) -> None:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            for dot in self.dots.values():
                if dot.on_focus : dot.set_over(True)
        
        if event.type == MOUSEBUTTONUP and event.button == 1:
            for dot in self.dots.values():
                if dot.on_focus:dot.set_over(False)

    def dots_update(self, surface, mouse_position) -> None:
        for dot in self.dots.values():
            if dot.on_focus and not dot.over:
                dot.set_color((0,255,0))    
            elif dot.over:
                dot.set_color((255,0,0))
                dot.set_position(mouse_position)
            else:
                dot.set_defaut_color() 
            dot.update(surface, mouse_position)   
    
    def quadratic_bezier_guidelines(self, surface) -> None:
        if self.is_quadratic:
            pygame.draw.line(surface, (0,255,0), self.dots["P0"].position, self.dots["P1"].position)
            pygame.draw.line(surface, (0,255,0), self.dots["P2"].position, self.dots["P1"].position)

    def cubic_bezier_guidelines(self, surface) -> None:
        if  not self.is_quadratic: 
            pygame.draw.line(surface, (0,255,0), self.dots["P0"].position, self.dots["P1"].position)
            #pygame.draw.line(surface, (0,255,0), self.dots["P1"].position, self.dots["P2"].position)
            pygame.draw.line(surface, (0,255,0), self.dots["P2"].position, self.dots["P3"].position) 

    def quadratic_bezier(self,dots,t):
        pos_P0 = dots["P0"].position
        pos_P1 = dots["P1"].position
        pos_P2 = dots["P2"].position
        
        x_final = (1 -t) ** 2 * pos_P0[0] + (1 -t) * 2 * t * pos_P1[0] + t * t * pos_P2[0]
        y_final = (1 -t) ** 2 * pos_P0[1] + (1 -t) * 2 * t * pos_P1[1] + t * t * pos_P2[1]

        return [x_final,y_final]

    def cubic_bezier(self,dots,t):
        pos_P0 = dots["P0"].position
        pos_P1 = dots["P1"].position
        pos_P2 = dots["P2"].position
        pos_P3 = dots["P3"].position
        
        x_final = (1 -t) ** 3 * pos_P0[0] + 3 * t *(1-t) ** 2 * pos_P1[0] + 3 * t ** 2 *(1-t) * pos_P2[0]+ t ** 3 * pos_P3[0]
        y_final = (1 -t) ** 3 * pos_P0[1] + 3 * t *(1-t) ** 2 * pos_P1[1] + 3 * t ** 2 *(1-t) * pos_P2[1]+ t ** 3 * pos_P3[1]

        return [x_final,y_final]

    def draw_bezier_cuve(self, surface, t_max, Q, show_guidelines) -> None:
        if show_guidelines:
            self.quadratic_bezier_guidelines(surface)
            self.cubic_bezier_guidelines(surface)
            
        func = self.quadratic_bezier if self.is_quadratic else self.cubic_bezier
        Q = 0.01 if Q <= 0.0 else Q
        t = 0
        t_next =Q
        while(t_max > t_next):
            point1 = func(self.dots,t)
            point2 = func(self.dots,t_next)

            pygame.draw.line(surface,(self.line_color),point1,point2)
            t += Q
            t_next += Q
          

    def update(self, surface, mouse_position, t_max, Q, show_guidelines) -> None:
         self.draw_bezier_cuve(surface, t_max, Q, show_guidelines)
         self.dots_update(surface, mouse_position)




