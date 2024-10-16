from events.choice_class import Choice
from events.consequence_class import Consequence
from events.event_class import Event
from society import society_class
from society.society_generation.create_random_society import create_random_society
from story_events.time_pass_events.one_year_passes import one_year_passes


soc=create_random_society()
one_year_passes(soc)
