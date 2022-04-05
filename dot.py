
import pygame

class Dot:
    def __init__(self,position:tuple, color:tuple, radius:int) -> None:
        super().__init__()
        self.position = position
        self.color = color
        self.defaut_color = color
        self.radius = radius
        self.over = False

    def set_over(self,state) -> None:
        self.over = state

    def set_color(self, color) -> None:
        self.color = color

    def set_defaut_color(self) -> None:
        self.color = self.defaut_color  

    def set_position(self, position) -> None:
        self.position = position    

    def is_on_focus(self, position) -> bool:
        deltaX = (self.position[0] - position[0]) ** 2
        deltaY = (self.position[1] - position[1]) ** 2

        return self.radius > (deltaX + deltaY) ** 0.5

    def draw(self, surface):
        pygame.draw.circle(surface,self.color,self.position,self.radius)
    