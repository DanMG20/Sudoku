import pygame as pg 
import style_settings

class Render:
    def __init__(self, game , screen ):
        self.game = game 
        self.screen = screen 
        self.square_size = 50
        self.quadrant_size = self.square_size*3
        self.clock_size = (150,50)
        

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

    def draw_end_game(self):
         self.screen.fill(style_settings.COLOR_END_SCREEN_BG)

        