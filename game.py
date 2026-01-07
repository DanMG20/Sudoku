import pygame as pg
import style_settings
from utils import resource_path
from event_manager import EventManager
from button import Button
from board import Board
from render import Render

class Game:
    """
    This class only handles the logic of the game, it doesn't draw
    """
    def __init__(self):
        pg.init()

        self.difficulty = ""
        self.clock_size = (210,60)
        self.square_size = 50
        self.quadrant_size = 150
        self.sudoku_screen = (660,450)
        self.screen = pg.display.set_mode((350,500))
        pg.display.set_caption("Soduku")
        icon = pg.image.load(resource_path("assets/sudoku.ico"))
        pg.display.set_icon(icon)
        self.event_manager = EventManager(self)
        self.board = None
        self.render = Render(self,self.screen)
        self.font_button = self.render.font_button
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

        self.gen_screen_buttons()
        self.create_menu_buttons()
        self.gen_continue_button()
        self.gen_end_game_button()
    

    def run(self): 
        clock = pg.time.Clock()
        running = True
        while running:
            self.screen.fill(style_settings.BG_COLOR)
            
            running = self.event_manager.manage_events()

            if self.in_menu:
                self.render.draw_menu()
            elif self.game_paused:
                self.render.draw_pause()
            elif self.game_over:
                self.render.draw_end_game()
            else:    
                self.render.draw_sudoku_board()
                self.render.draw_selected_square()
                self.render.draw_clock()
                self.render.draw_screen_buttons()
              
            pg.display.flip()
            clock.tick(60)

    def create_menu_buttons(self):
        easy_button = Button("Fácil",self.font_button,0,150)
        medium_button = Button("Normal",self.font_button,0,230)
        hard_button = Button("Difícil",self.font_button,50,310)

        self.menu_buttons = [easy_button,medium_button,hard_button]
        for button in self.menu_buttons: 
            button.rect.centerx = self.screen.get_width() // 2 

    def gen_screen_buttons(self):
                   
        self.buttons = {
            "Nuevo Juego": (
                            self.quadrant_size *3 + 5,self.clock_size[1]+5),
            "Reiniciar": (self.quadrant_size *3 + 5,
                          (self.clock_size[1]+5)*2),
            "Pausa" : (self.quadrant_size*3 +5,
                            (self.clock_size[1] +5)*3),
                      
        }
        for text, pos in self.buttons.items():
            button = Button(text, self.font_button, pos[0], pos[1])
            button.default_pos = button.rect.topleft
            self.screen_buttons.append(button)
            
                       
    def gen_continue_button(self):
            continue_button = Button("Continuar",
                                     self.font_button,self.screen.get_size()[0] // 3 ,
                                     self.screen.get_size()[1] // 2
                                     )
            self.continue_button = continue_button

    def gen_end_game_button(self):
            end_game_button = Button("Nuevo Juego",
                                     self.font_button,
                                     0,
                                     0
                                     )
            self.end_game_button = end_game_button

    def change_screen_settings(self):
        ANCHO_PANTALLA = self.sudoku_screen[0]
        ALTO_PANTALLA = self.sudoku_screen[1]
        self.screen = pg.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
        self.screen.fill(style_settings.BG_COLOR)
        self.gen_continue_button()

    def get_board(self):
        return self.board.board
    
    def manage_click_buttons(self, event):
        if self.in_menu:
            for button in self.menu_buttons:
                if button.is_clicked_event(event): 
                    self.handle_button_action(button.text)
            return
        if self.game_paused:
            if self.continue_button.is_clicked_event(event):
                self.handle_button_action(self.continue_button.text)
            return
        if self.game_over:
            if self.end_game_button.is_clicked_event(event):
                self.handle_button_action("Nuevo Juego")
            return
        
        for button in self.screen_buttons: 
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
        square_pos = (
        mouse_position[1] // self.square_size,
        mouse_position[0] // self.square_size,
        )
        if square_pos[0]<9 and square_pos[1]<9:
            self.board.select_square(square_pos)

    def manage_keyboard(self, key_pressed):
        if self.in_menu or self.board is None:
            return
        
        self.board.set_value(key_pressed)
        if self.board.is_sudoku_solved():
            self.game_over = True
            self.end_time_string = self.manage_clock()

    def manage_clock(self):
        """
        It calculates the time you're spending solving the sudoku
        """
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
    

    def manage_movement(self,arrow_key):
        if arrow_key  == "UP": 
            self.board.move_selection(0,-1)
        elif arrow_key == "DOWN":
            self.board.move_selection(0,1)
        elif arrow_key == "LEFT":
            self.board.move_selection(-1,0)
        elif arrow_key == "RIGHT":
            self.board.move_selection(1,0)
