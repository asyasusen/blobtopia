from blob.blob_generation.blob_creator import create_random_blob
from events.choice_class import Choice
from events.consequence_class import Consequence
from events.event_class import Event
from society import society_class
from society.society_generation.create_random_society import create_random_society
from blob.relationship.relationship_manager import Relationship_Manager
from time_manager.time_manager import Time_Manager

x= create_random_blob()
y= create_random_blob()
Relationship_Manager.blobs_meet(x,y)
rel1 = Relationship_Manager.get_relationship(x,y)
print(rel1.get_friend_score())
Time_Manager.pass_days(30)
print(rel1.get_friend_score())
Time_Manager.pass_days(30)
print(rel1.get_friend_score())