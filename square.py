class Square: 
    def __init__(self,position,value,its_hidden,its_fixed, its_wrong):
        self.position = position
        self.value = value 
        self.its_hidden = its_hidden
        self.clicked = False 
        self.its_fixed = its_fixed
        self.its_wrong = its_wrong 


    def was_clicked(self):
        return self.clicked
    
    def click(self):
        if not self.its_fixed:
            self.clicked = True 


