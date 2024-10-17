import random
from blob.blob_generation.blob_creator import create_random_blob
from events.choice_class import Choice
from events.consequence_class import Consequence
from events.event_class import Event
from events.event_manager import Event_Manager
from relationship.relationship_manager import Relationship_Manager
from relationship.relationship_modifier_class import Relationship_Modifier
from society import society_class
from society.society_generation.create_random_society import create_random_society
from stats.stat_manager_class import Stat_Manager
from stats.stat_modifier_class import Stat_Modifier
from stats.stat_of_object_class import Stat_Of_Object
from time_manager.time_manager import Time_Manager




# Create random blobs and establish initial relationship
x = create_random_blob()
y = create_random_blob()


Stat_Manager.add_modifier_to_stat_of_object( modifier =Stat_Modifier(reason="happy wife happy life", score_modifier=20),
                                            object=x, stat="happiness")