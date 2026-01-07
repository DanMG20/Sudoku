import pygame as pg 
import style_settings
class Render:
    """
    This class only draws the game, not includes logic
    """
    def __init__(self,game,screen):
        self.game = game
        self.gen_fonts()
        self.screen = screen 
        self.square_size = self.game.square_size
        self.quadrant_size = self.square_size*3
        self.clock_size = self.game.clock_size
        
    def gen_fonts(self):
        self.font_number = pg.font.Font(None, style_settings.NUMBER_FONT_SIZE)
        self.font_button = pg.font.Font(None, style_settings.BUTTON_FONT_SIZE)
        self.font_menu = pg.font.Font(None, style_settings.MENU_FONT_SIZE)
    
    def draw_text_centered(self,text, font, color, center):
        surface = font.render(text, True , color)
        rect = surface.get_rect(center=center)
        self.screen.blit(surface, rect)

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
                pg.draw.rect(self.screen, style_settings.COLOR_HOVER_BUTTON, quadrant_rect, 3)

    def draw_squares(self,x_screen,y_screen):
        cell_rect = pg.Rect(
            x_screen,
            y_screen,
            self.square_size,
            self.square_size
        )
        pg.draw.rect(self.screen, style_settings.COLOR_HOVER_BUTTON, cell_rect, 1)

    def select_color_square(self,square):
        if square.selected: 
            return style_settings.COLOR_SELECTED
        elif square.wrong:
            return  style_settings.COLOR_ERROR
        elif not square.fixed: 
            return style_settings.COLOR_NOT_FIXED_SQUARE
        else:
            return style_settings.COLOR_TEXT
        
    def draw_square(self,square):
        x_screen = square.position[1] * self.square_size
        y_screen = square.position[0] * self.square_size
        
        self.draw_squares(x_screen,y_screen)

        if square.hidden: 
            return
        color_text = self.select_color_square(square)
        self.draw_text_centered(str(square.value),
                                self.font_number,
                                color_text,
                                ( 
            x_screen+ self.square_size // 2,
            y_screen+ self.square_size // 2,   
                )
            )

    def draw_sudoku_board(self): 
        self.draw_quadrants()
        board =self.game.get_board()
        for row in board:
            for square in row:
                self.draw_square(square)

    def draw_selected_square(self):
        pos = self.game.board.selected_pos
        if pos is None:
            return
        
        row, col = pos


        x_screen = col * self.square_size
        y_screen = row * self.square_size
                    
        square_rect = pg.Rect(
                x_screen,
                y_screen,
                self.square_size,
                self.square_size
            )
        
        pg.draw.rect(
                self.screen, 
                style_settings.COLOR_SELECTED, 
                square_rect,
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
            style_settings.COLOR_HOVER_BUTTON,
            clock_rect,
            2
        )

        time_string = self.game.manage_clock()

        self.draw_text_centered(time_string,
                                self.font_number,
                                style_settings.COLOR_TEXT,
                                ( 
            x_screen+ self.clock_size[0] // 2,
            y_screen+ self.clock_size[1] // 2,
            
        )
        )

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


        self.draw_text_centered(
            end_game_string_top,
            self.font_menu,
            style_settings.COLOR_TEXT,
            (screen_w // 2 , screen_h // 3)
            )

        self.draw_text_centered(
            end_game_string_bottom,
            self.font_menu,
            style_settings.COLOR_TEXT,
            (screen_w // 2 , screen_h // 3 + 50)
            )
        
        new_game_button = self.game.end_game_button
        new_game_button.rect.center = (screen_w // 2, screen_h // 1.5)
        new_game_button.draw(self.screen)


    def draw_pause(self):
        self.screen.fill(style_settings.COLOR_END_SCREEN_BG)
        screen_w, screen_h = self.screen.get_size()
        pause_string = "PAUSA"

        self.draw_text_centered(
            pause_string,
            self.font_menu,
            style_settings.COLOR_TEXT,
            (screen_w // 2 , screen_h // 3)
            )

        self.draw_pause_button()


    def draw_menu(self):
        screen_w, screen_h = self.screen.get_size()
        sudoku_string = "SUDOKU"
        second_line_string ="Elige la dificultad para"
        third_line_string ="continuar"

        self.draw_text_centered(
            sudoku_string,
            self.font_menu,
            style_settings.COLOR_TEXT,
            (screen_w // 2 , 20)
            )
        
        self.draw_text_centered(
            second_line_string,
            self.font_menu,
            style_settings.COLOR_TEXT,
            (screen_w // 2 , 70)
            )

        self.draw_text_centered(
            third_line_string,
            self.font_menu,
            style_settings.COLOR_TEXT,
            (screen_w // 2 , 100)
            )

        self.draw_menu_buttons()