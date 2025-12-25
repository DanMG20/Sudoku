import logging

def setup_logger(): 

    logging.basicConfig(
        level=logging.DEBUG,
        format = "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler("sudoku.log", encoding="utf-8"),
            logging.StreamHandler()
        ] 
    )


setup_logger()