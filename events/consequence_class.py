# choice_class.py

class Consequence:
    def __init__(self, effected_object=None, field=None, effect=None, text=None, func=None ):
        self.effected_object= effected_object
        self.field=field
        self.effect= effect
        self.text = text
        self.func =func


    def apply(self):
        if self.effected_object is not None and self.field is not None and self. effect is not None:
            # Update the field by adding the effect
            if self.text:
                print(self.text)
            #USE EDIT_ IF THERE IS ONE
            if hasattr(self.effected_object, 'edit_'+self.field):
                func = getattr(self.effected_object, 'edit_'+self.field)
                func(self.effect)
            else:
                #USE GET_ IF THERE IS ONE
                if hasattr(self.effected_object, 'get_'+self.field):
                    func=  getattr(self.effected_object, 'get_'+self.field)
                    current_value= func()
                else:
                    current_value = getattr(self.effected_object, self.field)
                if isinstance(current_value, int):
                    setattr(self.effected_object, self.field, current_value + self.effect)
                elif isinstance(current_value, str):
                    setattr(self.effected_object, self.field, current_value)
        if self.func is not None:
            self.func()
        

