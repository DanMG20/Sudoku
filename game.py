import pygame as pg
import style_settings
from event_manager import EventManager
from button import Button
from board import Board
from render import Render
class Game: 
    def __init__(self):
        pg.init()

        self.difficulty = ""
        self.sudoku_screen = (660,450)
        self.screen = pg.display.set_mode((350,500))
        pg.display.set_caption("Soduku")
        # pygame.display.set_icon(<image>)
        self.event_manager = EventManager(self)
        self.board = None
        self.render = Render(self,self.screen)
        self.start_time = pg.time.get_ticks()
        self.paused_start_time = 0
        self.total_pause_time = 0
        self.game_over = False
        self.game_paused = False
        self.in_menu = True
        self.end_time_string = None
        self.continue_button = None
        self.menu_buttons = []
        
        self.screen_buttons = []
        self.clock_size = (150,60)
        self.quadrant_size = 150
        self.create_screen_buttons()
        self.create_main_buttons()
        self.create_continue_button()

    

    def run(self): 
        clock = pg.time.Clock()
        running = True
        while running:
            self.screen.fill(style_settings.BG_COLOR)
            
            running = self.event_manager.manage_events()
            if self.in_menu:
                self.render.draw_menu()
            else:
                if not self.game_over and not self.game_paused:
                    
                    self.render.draw_sudoku_board()
                    self.render.draw_select_square()
                    self.render.draw_clock()
                    self.render.draw_screen_buttons()
                elif self.game_paused:
                    self.render.draw_pause()
                else:
                    self.render.draw_end_game()
            pg.display.flip()
            clock.tick(60)

    def change_screen_settings(self):
        ANCHO_PANTALLA = self.sudoku_screen[0]
        ALTO_PANTALLA = self.sudoku_screen[1]
        self.screen = pg.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
        self.screen.fill(style_settings.BG_COLOR)
        pg.display.set_caption("Sudoku -- Menu")
        self.create_continue_button()

    def create_main_buttons(self):
        easy_button = Button("Fácil",150,0)
        medium_button = Button("Normal",230,0)
        hard_button = Button("Difícil",310,50)

        self.menu_buttons = [easy_button,medium_button,hard_button]
        for button in self.menu_buttons: 
            button.rect.centerx = self.screen.get_width() // 2 


    def get_board(self):
        return self.board.board
    
    def manage_click_buttons(self, event):
        for button in self.screen_buttons:
            if button.is_clicked_event(event): 
                self.handle_button_action(button.text)
        if self.continue_button.is_clicked_event(event):
            self.handle_button_action(self.continue_button.text)
        for button in self.menu_buttons: 
            if button.is_clicked_event(event):
                self.handle_button_action(button.text)
                
                
    def handle_button_action(self, button_text):
        if self.in_menu:   
            if button_text:
                self.difficulty = button_text
                self.board = Board(self.difficulty)
                self.in_menu = False
                self.change_screen_settings()
        else: 
            if button_text == "Nuevo Juego":
                self.reset_game()

            elif button_text == "Reiniciar": 
                self.board_reset()

            elif button_text == "Pausa":
                self.game_paused = True
                self.paused_start_time = pg.time.get_ticks()
        
            elif button_text == "Continuar":
                if self.game_paused:
                    self.game_paused = False
                    pause_duration = pg.time.get_ticks() - self.paused_start_time
                    self.total_pause_time += pause_duration

            
    def reset_game(self):
        self.screen = pg.display.set_mode((350,500))
        self.difficulty =""
        self.in_menu = True
        self.start_time = 0
        self.total_pause_time = 0 
        self.paused_start_time = 0
       
        self.end_time_string = None
        self.game_over = False
        self.start_time = pg.time.get_ticks()

    def board_reset(self):
        self.board.reset_board()
        self.start_time = pg.time.get_ticks()
        self.total_pause_time = 0 
        self.paused_start_time = 0

    def manage_click(self, mouse_position):
        if self.in_menu and self.board is None:
            return
        
        square_size = 50
        square_pos = (
        mouse_position[1] // square_size,
        mouse_position[0] // square_size,
        )
        if square_pos[0]<9 and square_pos[1]<9:
            self.board.manage_click(square_pos)

    def manage_keyboard(self, key_pressed):
        if self.in_menu or self.board is None:
            return
        
        self.board.set_value(key_pressed)

        if self.board.is_sudoku_solved():
            self.game_over = True
            self.end_time_string = self.manage_clock()

    def manage_clock(self):
        if self.game_paused:
            elapsed_time_ms = self.paused_start_time - self.start_time - self.total_pause_time
        else: 
            current_time = pg.time.get_ticks()
            elapsed_time_ms = current_time- self.start_time - self.total_pause_time

        total_seconds = elapsed_time_ms // 1000
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        time_string = f"{minutes:02}:{seconds:02}"
        return time_string
    
    def get_end_time(self):
        return self.end_time_string
    
    def create_screen_buttons(self):
                   
        buttons = {
            "Nuevo Juego": (self.clock_size[1]+5,
                            self.quadrant_size *3 + 5),
            "Reiniciar": ((self.clock_size[1]+5)*2,
                            self.quadrant_size *3 + 5),
            "Pausa" : ((self.clock_size[1] +5)*3,
                            self.quadrant_size*3 +5),
                      
        }
        for button in buttons:
            new_button = Button(button, buttons[button][0],buttons[button][1]) 
            self.screen_buttons.append(new_button)
    def create_continue_button(self):
            continue_button = Button("Continuar",self.screen.get_size()[0] // 3 ,self.screen.get_size()[1] // 2)
            self.continue_button = continue_button


