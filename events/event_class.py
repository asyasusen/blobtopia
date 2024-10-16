# event_class.py

import os


class Event:
    def __init__(self, title= "Death of the the king", description="he died", choices=[]):
        self.title= title
        self.description=description
        self.choices = choices

    def add_choice(self, choice):
        self.choices.append(choice)

    def trigger(self):
        width = os.get_terminal_size().columns
        print("=" * width)
        print(f"{self.title.center(40)}")
        print("_" * width)
        print(f"{self.description}\n")
        if len(self.choices)==1:
            self.choices[0].print()
            input("\nConfirm: ")
            self.pick(0)
        else:
            for i, choice in enumerate(self.choices, 0):
                print(f"{i}. ", end="")
                choice.print()
            print("_" * width)
            while len(self.choices)>1:
                try:
                    user_choice_index = int(input("\nEnter the number of your choice: "))

                    if 0 <= user_choice_index < len(self.choices):
                        self.pick(user_choice_index)
                        break
                    else:
                        print(f"Please enter a number between 0 and {len(self.choices)-1}.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        print("=" * width)
        
    def pick(self, choice_index ):
        self.choices[choice_index].pick()
        
