
from pygame.constants import MOUSEBUTTONDOWN,MOUSEBUTTONUP



def dots_update( dots,surface,mouse_position):
     for dot in dots:
        if dot.position_is_in(mouse_position) and not dot.over:
            dot.set_color((0,255,0))    
        elif dot.over:
            dot.set_color((255,0,0))
            dot.set_position(mouse_position)
        else:
            dot.set_defaut_color() 
        dot.update(surface) 
     return dots   


def mouse_clik(event,dots,mouse_position):
    if event.type==MOUSEBUTTONDOWN:
        if event.button==1:
            for dot in dots:
                if dot.position_is_in(mouse_position):
                    dot.set_over(True)
        
    if event.type==MOUSEBUTTONUP:
        if event.button==1:
            for dot in dots:
                if dot.over:
                    dot.set_over(False)
            


