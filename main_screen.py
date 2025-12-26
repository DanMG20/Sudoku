import pygame as pg
from button import Button
import style_settings
class MainScreen: 
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((350,500))
        pg.display.set_caption("Soduku - Dificultad")
        # pygame.display.set_icon(<image>)

        self.gen_menu_buttons()

    def gen_menu_buttons(self):
        easy_button = Button("Fácil",150,0)
        medium_button = Button("Normal",230,0)
        hard_button = Button("Difícil",310,50)

        self.menu_buttons = [easy_button,medium_button,hard_button]

        for button in self.menu_buttons: 
            button.rect.centerx = self.screen.get_width() // 2 

    def draw_difficulty_buttons(self): 
        
        for button in self.menu_buttons: 
            button.draw(self.screen)

    def run(self):
        running = True
        while running:
            self.screen.fill(style_settings.BG_COLOR)

            self.draw_difficulty_buttons()
            running = self.manage_events(self.menu_buttons)
            pg.display.flip()

    def manage_events(self, menu_buttons):
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return False 
        
            for button in menu_buttons: 
                if button.is_clicked_event(event): 
                    self.difficulty = button.text
        return True
    
    def get_difficulty(self): 
        return self.difficulty