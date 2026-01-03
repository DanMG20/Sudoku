class Square: 
    """
    It Represents an individual square of the Sudoku board.

    Stores its position, value and states such as: 
    - whether it's hidden
    - whether it's fixed
    - whether it's selected
    - whether it's incorrect
    """

    def __init__(self,
                position,
                value = 0,
                hidden = True,
                fixed = False,
                wrong = False
                ):
        self.position = position
        self.value = value 
        self.hidden = hidden
        self.selected = False 
        self.fixed = fixed
        self.wrong = wrong 

    def select(self):
        if self.fixed: 
            return 
        self.selected = True


    def deselect(self): 
        if self.fixed: 
            return
        self.selected  = False
    def set_value(self, new_value):
        if self.fixed:
            return 
        self.value = new_value
    def hide(self):
        self.hidden  = True 
    def unhide(self):
        self.hidden = False
    def set_wrong(self):
        self.wrong = True
    def set_not_wrong(self):
        self.wrong = False

