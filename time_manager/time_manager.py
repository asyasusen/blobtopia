from events.choice_class import Choice
from events.consequence_class import Consequence
from events.event_class import Event
from events.choice_class import Choice



class Time_Manager:
    day_count=1
    
    @classmethod
    def pass_days(cls, day=1):
        cls.day_count+=day
    @classmethod
    def get_time(cls):
        return cls.day_count
