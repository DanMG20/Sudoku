import pygame as pg 
import style_settings
from button import Button
class Render:
    def __init__(self, game , screen ):
        self.game = game 
        self.screen = screen 
        self.square_size = 50
        self.quadrant_size = self.square_size*3
        self.clock_size = (210,60)
    
    def draw_quadrants(self):
        for row in range(3):
            for column in range(3):
                start_row_quadrant = row * self.quadrant_size
                start_column_quadrant = column  * self.quadrant_size

                quadrant_rect = pg.Rect(
                    start_column_quadrant,
                    start_row_quadrant, 
                    self.quadrant_size,
                    self.quadrant_size
                )
                pg.draw.rect(self.screen, style_settings.COLOR_HOVER, quadrant_rect, 3)

    def draw_squares(self,x_screen,y_screen):


                cell_rect = pg.Rect(
                    x_screen,
                    y_screen,
                    self.square_size,
                    self.square_size
                )
                pg.draw.rect(self.screen, style_settings.COLOR_HOVER, cell_rect, 1)
  

    def draw_sudoku_board(self): 

        self.draw_quadrants()
        board =self.game.get_board()
        for row in board:
            for square in row:
                x_screen = square.position[1] * self.square_size
                y_screen = square.position[0] * self.square_size
                
                self.draw_squares(x_screen,y_screen)

                if square.its_hidden: 
                    continue
                elif square.clicked: 
                     color_text = style_settings.COLOR_SELECTED
                elif square.its_wrong:
                     color_text = style_settings.COLOR_ERROR
                elif not square.its_fixed: 
                     color_text = style_settings.COLOR_NOT_FIXED_SQUARE
                else:
                     color_text = style_settings.COLOR_TEXT
                text_surface = style_settings.NUMBER_FONT.render(
                    str(square.value),
                        True ,
                        color_text
                        )
                rect = text_surface.get_rect()

        

                rect.center = ( 
                    x_screen+ self.square_size // 2,
                    y_screen+ self.square_size // 2,
                    
                )
                
    
                self.screen.blit(text_surface, rect)

    def draw_select_square(self):
        board = self.game.get_board()
        for row in board:
            for square in row:
                    if square.clicked:
                            
                        x_screen = square.position[1] * self.square_size
                        y_screen = square.position[0] * self.square_size
                    
                        cell_rect = pg.Rect(
                                x_screen,
                                y_screen,
                                self.square_size,
                                self.square_size
                            )
                        pg.draw.rect(
                                self.screen, 
                                style_settings.COLOR_SELECTED, 
                                cell_rect,
                                4
                                )
                    
    def draw_clock(self):
        x_screen = self.quadrant_size * 3 
        y_screen = 0
        clock_rect= pg.Rect(
            x_screen,
            y_screen,
            self.clock_size[0],
            self.clock_size[1]

        )
        pg.draw.rect(
            self.screen,
            style_settings.COLOR_HOVER,
            clock_rect,
            2
        )

        time_string = self.game.manage_clock()

        time_surface = style_settings.NUMBER_FONT.render(
             time_string,
             True,
             style_settings.COLOR_TEXT
             )
        
        rect = time_surface.get_rect()

        

        rect.center = ( 
            x_screen+ self.clock_size[0] // 2,
            y_screen+ self.clock_size[1] // 2,
            
        )
        

        self.screen.blit(time_surface, rect)

    def draw_screen_buttons(self):
        for button in self.game.screen_buttons:
            button.draw(self.screen)
    def draw_menu_buttons(self):
        for button in self.game.menu_buttons:
            button.draw(self.screen)
    def draw_pause_button(self):
         self.game.continue_button.draw(self.screen)

    def draw_end_game(self):
        self.screen.fill(style_settings.COLOR_END_SCREEN_BG)
        screen_w, screen_h = self.screen.get_size()

        time_string = self.game.get_end_time()
        
        end_game_string_top = "Resolviste el sudoku!"
        end_game_string_bottom = f"Solo te tomó {time_string} minutos"

        text_top = style_settings.BUTTON_FONT.render(
             end_game_string_top, 
             True, 
             style_settings.COLOR_TEXT
             )
        
        text_top_rect = text_top.get_rect(center = (screen_w // 2 , screen_h // 3))
        self.screen.blit(text_top, text_top_rect)

        text_bottom = style_settings.BUTTON_FONT.render(
             end_game_string_bottom,
             True,
             style_settings.COLOR_TEXT
        )

        text_bottom_rect = text_bottom.get_rect(center = (screen_w // 2 , screen_h // 3 + 50))
        self.screen.blit(text_bottom, text_bottom_rect)
        new_game_button = self.game.screen_buttons[0]
        new_game_button.rect.center = (screen_w // 2, screen_h // 1.5)
        new_game_button.draw(self.screen)

    def draw_pause(self):
        self.screen.fill(style_settings.COLOR_END_SCREEN_BG)
        screen_w, screen_h = self.screen.get_size()
        pause_string = "PAUSA"

        pause_text = style_settings.BUTTON_FONT.render(
             pause_string, 
             True, 
             style_settings.COLOR_TEXT
             )
        
        pause_rect = pause_text.get_rect(center = (screen_w // 2 , screen_h // 3))
        self.screen.blit(pause_text, pause_rect)

        self.draw_pause_button()

    def draw_menu(self):
        screen_w, screen_h = self.screen.get_size()
        sudoku_string = "SUDOKU"
        second_line_string ="Elige la dificultad para"
        third_line_string ="continuar"

        sudoku_text = style_settings.NUMBER_FONT.render(
             sudoku_string, 
             True, 
             style_settings.COLOR_TEXT
             )
        
        second_line_text = style_settings.MENU_FONT.render(
             second_line_string, 
             True, 
             style_settings.COLOR_TEXT
             )

        third_line_text = style_settings.MENU_FONT.render(
             third_line_string, 
             True, 
             style_settings.COLOR_TEXT
             )
        
        
            
            
        
        sudoku_rect = sudoku_text.get_rect(center = (screen_w // 2 , 20))
        self.screen.blit(sudoku_text, sudoku_rect)

        second_line_rect = second_line_text.get_rect(center = (screen_w // 2 , 70))
        self.screen.blit(second_line_text, second_line_rect)

        third_line_rect = third_line_text.get_rect(center = (screen_w // 2 , 100))
        self.screen.blit(third_line_text, third_line_rect)




        self.draw_menu_buttons()