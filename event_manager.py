import pygame as pg

class EventManager: 
    def __init__(self,game):
        self.game = game 

    def manage_events(self):
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return False 
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.handle_mouse(event)
            elif event.type == pg.KEYDOWN:
                self.handle_keyboard(event)
        return True
    
    def handle_mouse(self,event):
        self.game.manage_click(pg.mouse.get_pos())
        self.game.manage_click_buttons(event)

    def handle_keyboard(self, event):
        number_key = self.handle_key(event)
        if number_key is not None:
            self.game.manage_keyboard(number_key)
        self.handle_move(event)

    def handle_key(self,event):
        if pg.K_1 <=event.key <= pg.K_9:
            number_key = event.key - pg.K_0
            return number_key
        elif pg.K_KP1 <=event.key <= pg.K_KP9:
            number_key =    event.key - pg.K_KP_0 +10
            return number_key
        elif event.key == pg.K_BACKSPACE or event.key ==pg.K_DELETE:
            return 0 
        return None

    def handle_move(self,event):
        if event.key == pg.K_DOWN:
            self.game.manage_movement("DOWN")
        elif event.key == pg.K_LEFT:
            self.game.manage_movement("LEFT")
        elif event.key == pg.K_UP:
            self.game.manage_movement("UP")
        elif event.key == pg.K_RIGHT:
           self.game.manage_movement("RIGHT")