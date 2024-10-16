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
    ####TODO DELETE THIS, ONLY FOR REFERANCE
    def one_year_passes(my_society):
        next_year_event= Event("Time passes","No matter what we do, we cannot slow down the passage of time. ")
        next_year_choice = Choice("let the year end")
        next_year_event.add_choice(next_year_choice)
        for x in my_society.members:
            age_up_consq = Consequence(x, "age", 1, f"{x.name} ages." )
            next_year_choice.add_consequence(age_up_consq)
        next_year_event.trigger()