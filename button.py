
import pygame

pygame.init()


class Button():
    def __init__(self,label,size,position):
        super().__init__()
        self.size = size
        self.position = position
        self.label = label

    def draw_button(self,surface):
        pygame.draw.rect(surface,(255,0,0),(self.position,self.size),0)
    
        text_font = pygame.font.SysFont("monospace",20)
        text = text_font.render(self.label,1,(255,255,255),False)
        surface.blit(text,self.position)
        



    def contact(self,position):
        if position[0] > self.position[0]and position[0] < self.size[0] + self.position[0]:
             if position[1] > self.position[1]and position[1] < self.size[1] + self.position[1]:
                 return True
        return False
