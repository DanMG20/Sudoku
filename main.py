from game import Game 
from main_screen import MainScreen
def main():
    #Configuracion inicial 
    difficulty = "Normal" 

    instance_game = Game(difficulty)
    instance_game.run()



if __name__ == "__main__": 
    main()