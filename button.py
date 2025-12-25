import pygame as pg 


class Button(): 

    def __init__(self, text,position_y,position_x):
        self.text = text
        self.COLOR_IDLE = (74, 93, 107)
        self.FONT = pg.font.SysFont(None, 36)
        self.COLOR_HOVER = (58, 74, 84)
        self.rect = pg.Rect(position_x,position_y,200,60)
        self.COLOR_TEXT = (242, 247, 252)


    def draw(self, surface):
        mouse_position = pg.mouse.get_pos()
        color = self.COLOR_HOVER if self.rect.collidepoint(mouse_position) else self.COLOR_IDLE

        pg.draw.rect(surface, color, self.rect , border_radius = 8)
        text_surface = self.FONT.render (self.text, True, self.COLOR_TEXT)
        text_rect = text_surface.get_rect (center = self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked_event(self, event): 
        return event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
