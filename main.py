import pygame as pg 
from button import Button
import logger_config

def start_game():

    pg.init()

        #configurar el ancho y el ato de la pantalla
    #MAYUSCULAS SIGNIFICAN QUE ESTAS VARIABLES SE MANTENDRAN CONSTANTES
    ANCHO_PANTALLA = 350
    ALTO_PANTALLA = 500
    screen = pg.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
    #Titulo e icono
    pg.display.set_caption("Sudoku")
   
    running = True
    clock = pg.time.Clock()

                
    easy_button = Button("Fácil",150,0)
    #easy_button.rect.centerx = screen.get_width() // 2 
    medium_button = Button("Normal",230,0)
    hard_button = Button("Difícil",310,50)

    menu_buttons = [easy_button,medium_button,hard_button]

    for button in menu_buttons: 
        button.rect.centerx = screen.get_width() // 2 



    while running: 
        
        screen.fill("gray")

        for button in menu_buttons:  
            button.draw(screen)
     
        #AQUI VAN LOS EVENTOS MIENTRAS CORRE 

        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                running =False

        for button in menu_buttons: 
            if button.is_clicked_event(event): 
                print(f"Botón {button.text} presionado")


        #----------------------------------BOTONES-------------------------------------------
        

        

        # SE RENDERIZA EL JUEGO AQUI 

        pg.display.flip()

        clock.tick(60)

    pg.quit()

if __name__ == "__main__":

    start_game()
