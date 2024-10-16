# choice_class.py

class Consequence:
    def __init__(self, effected_object, field, effect, text="people got happy" ):
        self.effected_object= effected_object
        self.field=field
        self.effect= effect
        self.text = text


    def apply(self):
        # Get the current value of the field
        # Update the field by adding the effect
        if self.text:
            print(self.text)
        if hasattr(self.effected_object, 'edit_'+self.field):
            func = getattr(self.effected_object, 'edit_'+self.field)
            func(self.effect)
        else:
            current_value = getattr(self.effected_object, self.field)
            if isinstance(current_value, int):
                setattr(self.effected_object, self.field, current_value + self.effect)
            elif isinstance(current_value, str):
                setattr(self.effected_object, self.field, current_value)
        

