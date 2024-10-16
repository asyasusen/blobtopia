
from blob.blob_generation.blob_creator import create_random_blob
from society.society_class import Society

def create_random_society(name="Maviler", num_of_members=10):
    my_society = Society(name ="Maviler")
    for i in range(10):
        x=create_random_blob()
        my_society.add_member(x)
    return my_society

