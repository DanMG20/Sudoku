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
                self.game.manage_click_buttons(event)

            if event.type == pg.KEYDOWN:
                if pg.K_1 <=event.key <= pg.K_9:

                    number = event.key - pg.K_0
                    self.game.manage_keyboard(number)
                elif pg.K_KP1 <=event.key <= pg.K_KP9:

                    number =    event.key - pg.K_KP_0 +10
                    self.game.manage_keyboard(number)
                elif event.key == pg.K_BACKSPACE or event.key ==pg.K_DELETE:
                    self.game.manage_keyboard(0)

                elif event.key == pg.K_DOWN:
                    self.game.board.move_selection(0,1)
                elif event.key == pg.K_LEFT:
                    self.game.board.move_selection(-1,0)
                elif event.key == pg.K_UP:
                    self.game.board.move_selection(0,-1)
                elif event.key == pg.K_RIGHT:
                    self.game.board.move_selection(1,0)
                  
        
                    
                
        return True