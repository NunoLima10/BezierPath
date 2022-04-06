from telnetlib import DO
import pygame
from pygame.constants import MOUSEBUTTONDOWN,MOUSEBUTTONUP
from dot import Dot
from random import randint


class BezierPath:
    def __init__(self, dot_color:tuple, line_color:tuple) -> None:
        super().__init__()

        #dot
        self.dot_color = dot_color
        self.dot_seleced_color = (0,255,0)
        self.dot_over_color = (255,0,0)
        self.dot_radis = 8
        
        #controle dot
        self.cotrole_dot_color = (200,200,200)
        self.cotrole_dot_seleced_color = (0,255,0)
        self.cotrole_dot_over_color = (255,0,0)
        self.controle_dot_radis = 5

        #line
        self.line_color = line_color
        self.bezier_path = []

        self.dots = [
            Dot((200,200), self.dot_color, self.dot_radis),
            Dot((500,500), self.cotrole_dot_color, self.controle_dot_radis),
            Dot((600,500), self.cotrole_dot_color, self.controle_dot_radis),
            Dot((300,200), self.dot_color, self.dot_radis)
        ]

    def mouse_trigger(self, event) -> None:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            for dot in self.dots:
                if dot.on_focus : dot.toggle_over_state()
        
        if event.type == MOUSEBUTTONUP and event.button == 1:
            for dot in self.dots:
                if dot.on_focus : dot.toggle_over_state()
                    
    def dots_update(self, surface, mouse_position) -> None:
        pygame.draw.line(surface, (0,255,0), self.dots[0].position, self.dots[1].position)
        pygame.draw.line(surface, (0,255,0), self.dots[2].position, self.dots[3].position) 

        for dot in self.dots:
            if dot.on_focus and not dot.over:
                dot.set_seleced_color()    
            elif dot.over:
                dot.set_over_color()
                dot.set_position(mouse_position)
            else:
                dot.set_defaut_color() 
            dot.update(surface, mouse_position)

    def cubic_bezier(self,dots,t) -> list:
        
        x_final = (1 -t) ** 3 * dots[0].position_x + 3 * t *(1-t) ** 2 * dots[1].position_x + 3 * t ** 2 *(1-t) * dots[2].position_x + t ** 3 * dots[3].position_x
        
        y_final = (1 -t) ** 3 * dots[0].position_y + 3 * t *(1-t) ** 2 * dots[1].position_y + 3 * t ** 2 *(1-t) * dots[2].position_y + t ** 3 * dots[3].position_y

        return [x_final,y_final]

    
    def generate_path(self)-> None:
        self.bezier_path.clear()
        t = 0
        next_t =0.01
  
        while(1 > next_t):
            point = self.cubic_bezier(self.dots,t)
            next_point = self.cubic_bezier(self.dots,next_t)
            t += 0.01
            next_t += 0.01 
            self.bezier_path.append(point)
            self.bezier_path.append(next_point)
            


    def draw_bezier_path(self, surface) -> None:

        self.generate_path()
        numebr_of_poitns = len(self.bezier_path) -1

        for point_index in range(numebr_of_poitns):
            point = self.bezier_path[point_index]
            next_point = self.bezier_path[point_index + 1] if point_index < numebr_of_poitns else self.bezier_path[point_index]
            pygame.draw.line(surface, (self.line_color),point ,next_point)
           

    def update(self, surface, mouse_position, ) -> None:
        self.draw_bezier_path(surface)
        self.dots_update(surface, mouse_position)
         