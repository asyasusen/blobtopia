
from relationship.relationship_modifier_class import Relationship_Modifier
from time_manager.time_manager import Time_Manager


class Relationship:
    def __init__(self,blob_feels, blob_towards):
        self.blob_feels = blob_feels
        self.blob_towards = blob_towards
        self.modifiers=[]
    def add_modifier(self, modifier):
        self.modifiers.append(modifier)
    def remove_modifier(self, modifier):
        self.modifiers.remove(modifier)
    def get_friend_score(self):
        return self.calculate_score("friend")
    def get_romance_score(self):
        return self.calculate_score("romance")
    def calculate_score(self, type):
        score = 0
        time = Time_Manager.get_time()
        for i in range(len(self.modifiers) - 1, -1, -1):
            modifier = self.modifiers[i]
            if modifier.time_limit is None or time - modifier.start_time <= modifier.time_limit:
                change = getattr(modifier, type + "_score_modifier")
                score += change
            else:
                #modifier is not active anymore
                self.modifiers.pop(i)  # Remove expired modifier
        return score

                    
        