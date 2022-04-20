
import pygame
from pygame.constants import MOUSEBUTTONDOWN,MOUSEBUTTONUP
from dot import Dot
from math import floor


class BezierPath:
    def __init__(self,start_position:tuple, dot_color:tuple, line_color:tuple, max_Width:int, max_height) -> None:
        super().__init__()

        #screen
        self.max_width = max_Width
        self.max_height = max_height

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

        #bezier_path
        self.line_color = line_color
        self.bezier_path = []

        self.dots = [Dot(start_position, self.dot_color, self.dot_radis)]
        self.number_of_dots = 1

    def mouse_trigger(self, event) -> None:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            for dot in self.dots:
                if dot.on_focus : dot.toggle_over_state()
        
        if event.type == MOUSEBUTTONUP and event.button == 1:
            for dot in self.dots:
                if dot.on_focus : dot.toggle_over_state()

    def dots_update(self, surface, mouse_position,show_dots) -> None:
        for dot in self.dots:
            if dot.on_focus and not dot.over:
                dot.set_seleced_color()    
            elif dot.over:
                dot.set_over_color()
                dot.set_position(mouse_position)
            else:
                dot.set_defaut_color() 
            dot.update(surface, mouse_position,show_dots)

    def add_dots(self,mouse_position, controle_dot1_position,controle_dot2_position)-> None:

        controle_dot1 = Dot(controle_dot1_position, self.cotrole_dot_color, self.controle_dot_radis)
        controle_dot2 = Dot(controle_dot2_position, self.cotrole_dot_color, self.controle_dot_radis)
        dot = Dot(mouse_position, self.dot_color, self.dot_radis)

        self.dots.append(controle_dot1)
        self.dots.append(controle_dot2)
        self.dots.append(dot)

    def limit_to_screen_size(self,position_x, position_y) -> tuple:

        if position_x >= self.max_width : position_x = self.max_width - self.controle_dot_radis - 5 
        if position_x <= 0 : position_x = self.dot_radis + 5 

        if position_y >= self.max_height : position_y = self.max_height - self.dot_radis - 5 
        if position_y <= 0 : position_y =self.dot_radis + 5 

        return (position_x, position_y)   


    def generate_new_dot(self,mouse_position,) -> None:
        for dot in self.dots: 
            if dot.on_focus : return
        
        if self.number_of_dots == 1:
            firt_dot = self.dots[0]
            #firts controle dot
            controle_dot1_position_x = firt_dot.position_x 
            controle_dot1_position_y = firt_dot.position_y - 100 
            controle_dot1_position = self.limit_to_screen_size(controle_dot1_position_x, controle_dot1_position_y)
            #second controle dot
            controle_dot2_position_x = mouse_position[0]
            controle_dot2_position_y = mouse_position[1] - 100
            controle_dot2_position = self.limit_to_screen_size(controle_dot2_position_x, controle_dot2_position_y)

            self.add_dots(mouse_position,controle_dot1_position, controle_dot2_position)   
        else:
            last_dot = self.dots[-1]
            last_controle_dot =  self.dots[-2]
            #firts controle dot
            controle_dot1_position_x = last_dot.position_x + last_dot.position_x - last_controle_dot.position_x
            controle_dot1_position_y = last_dot.position_y + last_dot.position_y - last_controle_dot.position_y
            controle_dot1_position = self.limit_to_screen_size(controle_dot1_position_x, controle_dot1_position_y)
            #second controle dot
            controle_dot2_position_x = floor(2*mouse_position[0] - abs(mouse_position[0] + last_controle_dot.position_x) / 2)
            controle_dot2_position_y = floor(2*mouse_position[1] - abs(mouse_position[1] + last_controle_dot.position_y) / 2 )
            controle_dot2_position = self.limit_to_screen_size(controle_dot2_position_x, controle_dot2_position_y)

            self.add_dots(mouse_position,controle_dot1_position, controle_dot2_position)
    
    def quadratic_bezier(self,dots,t):
        
        x_final = (1 -t)**2 * dots[0] + (1 -t)*2 * t * dots[0] + t*t * dots[0]
        y_final = (1 -t)**2 * dots[1] + (1 -t)*2 * t * dots[1] + t*t * dots[1]

        return [x_final,y_final]

    def cubic_bezier(self,dots,t) -> list:
        
        x_final = (1 -t) **3 * dots[0].position_x + 3*t * (1-t)**2 * dots[1].position_x + 3 * t**2 *(1-t) * dots[2].position_x + t**3 * dots[3].position_x
        
        y_final = (1 -t) **3 * dots[0].position_y + 3*t * (1-t)**2 * dots[1].position_y + 3 * t**2 *(1-t) * dots[2].position_y + t**3 * dots[3].position_y

        return [x_final,y_final]

    
    def generate_path(self,t_max,Q)-> None:
        self.bezier_path.clear()
        t = 0
        next_t =0.01
  
        for i,_ in enumerate(self.dots):
            if i*3  >= self.number_of_dots - 1 : break
            
            dots_segment =[self.dots[i*3], self.dots[i*3 + 1] , self.dots[i*3 + 2], self.dots[i*3 + 3]]
            t = 0
            next_t = Q
            while(t_max > next_t):
                point = self.cubic_bezier(dots_segment,t)
                next_point = self.cubic_bezier(dots_segment,next_t)
                t += Q
                next_t += Q
                self.bezier_path.append(point)
                self.bezier_path.append(next_point)
            if i*3 + 3  >= self.number_of_dots - 1 : break


    def draw_bezier_path(self, surface, t_max, Q) -> None:

        self.generate_path(t_max, Q)
        numebr_of_poitns = len(self.bezier_path) - 1

        for point_index in range(numebr_of_poitns):
            point = self.bezier_path[point_index]
            next_point = self.bezier_path[point_index + 1] if point_index < numebr_of_poitns else self.bezier_path[point_index]
            pygame.draw.line(surface, (self.line_color),point ,next_point)
    
    def draw_guidelines(self,surface)-> None:
        for i,_ in enumerate(self.dots):
            if i * 3  >= self.number_of_dots - 1 : break
            dots_segment =[self.dots[i*3], self.dots[i*3 + 1] , self.dots[i*3 + 2], self.dots[i*3 + 3]]
            pygame.draw.line(surface, (0,255,0), dots_segment[0].position, dots_segment[1].position)
            pygame.draw.line(surface, (0,255,0), dots_segment[2].position, dots_segment[3].position) 
            if i * 3 + 3  >= self.number_of_dots - 1 : break
           

    def update(self, surface, mouse_position, t_max, Q, show_guidelines,show_dots) -> None:
         self.draw_bezier_path(surface, t_max, Q)

         if show_guidelines: self.draw_guidelines(surface)

         self.dots_update(surface, mouse_position,show_dots)
         self.number_of_dots = len( self.dots)
         