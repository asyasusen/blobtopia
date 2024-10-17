# choice_class.py




class Consequence:
    def __init__(self, effected_object=None, field=None, effect=None, text=None, func=None, stat=None ):
        self.effected_object= effected_object
        self.field=field
        self.effect= effect
        self.text = text
        self.func =func


    def apply(self):
        if self.func is not None:
            self.func()
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
                    current_value = getattr(self.effected_object, self.field, None)
                if isinstance(current_value, int):
                    setattr(self.effected_object, self.field, current_value + self.effect)
                elif isinstance(current_value, str):
                    setattr(self.effected_object, self.field, current_value)
                elif current_value is None:
                    from stats.stat_manager_class import Stat_Manager
                    Stat_Manager().add_modifier_to_stat_of_object(object=self.effected_object,
                                                                  stat= self.field,
                                                                  modifier=self.effect)

        

