import pygame as pg

class EventManager: 
    def __init__(self,game):
        self.game = game 


    def manage_events(self):
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return False 
            
            if event.type == pg.MOUSEBUTTONDOWN:
                self.game.manage_click(pg.mouse.get_pos())

            if event.type == pg.KEYDOWN:
                if pg.K_1 <=event.key <= pg.K_9:

                    number = event.key - pg.K_0
                    self.game.manage_keyboard(number)
                elif pg.K_KP1 <=event.key <= pg.K_KP9:

                    number =    event.key - pg.K_KP_0 +10
                    self.game.manage_keyboard(number)
                elif event.key == pg.K_BACKSPACE:
                    self.game.manage_keyboard(0)
                    
                
        return True