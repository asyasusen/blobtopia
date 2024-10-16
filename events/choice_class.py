# choice_class.py

class Choice:
    def __init__(self, text= "build him a graveyard", consequences=[] ):
        self.text=text
        self.consequences= consequences
    def add_consequence(self, consequence):
        self.consequences.append(consequence)
    def pick(self):
        self.print()
        for consequence in self.consequences:
            consequence.apply()
    def print(self):
        print(self.text)

        
