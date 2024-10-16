# society_class.py

class Society:
    def __init__(self, name="Society of blobs"):
        self.members=[]
        self.name=name
        self.compassion=50
        
    def add_member(self,blob):
        self.members.append(blob)

    def __str__(self):
        x=""
        for member in self.members:
            x+=member.__str__()
        return x