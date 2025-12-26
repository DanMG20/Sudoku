import pygame as pg
import style_settings
from event_manager import EventManager
from button import Button
from board import Board
from render import Render
class Game: 
    def __init__(self,difficulty):
        pg.init()

        self.difficulty = difficulty
        self.screen = pg.display.set_mode((600,450))
        pg.display.set_caption("Soduku")
        # pygame.display.set_icon(<image>)
        self.event_manager = EventManager(self)
        self.board = Board(difficulty)
        self.render = Render(self,self.screen)
        self.start_time = pg.time.get_ticks()
        self.game_over = False




    def run(self): 
        clock = pg.time.Clock()
        running = True
        while running:
            self.screen.fill(style_settings.BG_COLOR)
            
            running = self.event_manager.manage_events()

            if not self.game_over:
                self.render.draw_sudoku_board()
                self.render.draw_select_square()
                self.render.draw_clock()
            else:
                self.render.draw_end_game()
            pg.display.flip()
            clock.tick(60)


    def get_board(self):
        return self.board.board
    

    def manage_click(self, mouse_position):
        square_size = 50
        square_pos = (
        mouse_position[1] // square_size,
        mouse_position[0] // square_size,
        )
        if square_pos[0]<9 and square_pos[1]<9:
            self.board.manage_click(square_pos)
    def manage_keyboard(self, key_pressed):
        self.board.set_value(key_pressed)

        if self.board.is_sudoku_solved():
            self.game_over = True

    def manage_clock(self):
        current_time = pg.time.get_ticks()
        elapsed_time_ms = current_time- self.start_time
        total_seconds = elapsed_time_ms // 1000
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        time_string = f"{minutes:02}:{seconds:02}"
        return time_string

