from blob.blob_class import *
from blob.blob_generation.name_generation.name_generator import pick_random_name

import random
def create_random_blob():
    name = pick_random_name()
    age = random.randint(0,100)
    x = Blob(name=name, age=age)
    return  x


