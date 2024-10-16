import pickle
import os
import random
# Run this once to create the pickle file from txt file
def save_names_file_as_pickle(file_name="random_names.txt", new_name="random_names.pkl"):
    # Load names from the text file and clean them up

    with open(get_file_path(file_name), "r") as file:
        names = [name.strip() for name in file if name.strip()]

    # Save the list to a binary file
    with open(get_file_path(new_name), "wb") as pickle_file:
        pickle.dump(names, pickle_file)
    save_names_file_as_pickle()

def load_names_from_pickle(file_name="random_names.pkl"):
    with open(get_file_path(file_name), "rb") as pickle_file:
        names = pickle.load(pickle_file)
    return names

def get_file_path(file_name):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    return os.path.join(__location__, file_name)

def pick_random_name():
    names = load_names_from_pickle()
    return random.choice(names)

