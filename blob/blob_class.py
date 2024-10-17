# blob_class.py

# natural_death_age+-natural_death_age_gap  will be the time blobs die
import random


natural_death_age=80
natural_death_age_gap=20


class Blob:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.alive= True
        self.happiness=0


    def __str__(self):
        return f"[blob: {self.name}-{self.age}]"
    
    def die(self):
        self.alive = False
        print(f"{self.name} has passed away :( at the age of {self.age}")

    def edit_age(self, year):
        if self.alive:
            self.age+=year
            if(self.age>natural_death_age+ random.randint(-natural_death_age_gap, natural_death_age_gap)):
                self.die()
