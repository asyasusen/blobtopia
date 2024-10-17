# choice_class.py

class Choice:
    def __init__(self, text= "build him a graveyard" ):
        self.text=text
        self.consequences=[]
    def add_consequence(self, consequences): #can be array or item
        if isinstance(consequences, list):
            self.consequences.extend(consequences)
        else:
            self.consequences.append(consequences)
    def pick(self):
        self.print()
        for consequence in self.consequences:
            consequence.apply()
    def print(self):
        print(self.text)

        
