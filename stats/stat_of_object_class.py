
from stats.stat_modifier_class import Stat_Modifier
from time_manager.time_manager import Time_Manager
import inspect

class Stat_Of_Object:
    def __init__(self,object, stat):
        from stats.stat_manager_class import Stat_Manager
        self.object = object
        self.stat = Stat_Manager.__stat_string_or_object_give_object__(stat)
        self.stat_name = self.stat.stat_name
        self.modifiers=[]
        Stat_Manager.__check_if_object_has_stats__( object)
        self.object.stats.append(self)

    def add_modifier(self, modifier):
        if isinstance(modifier, Stat_Modifier):
            self.modifiers.append(modifier)
        else:
            raise ValueError("Modifier class not given.")
    def remove_modifier(self, modifier):
        self.modifiers.remove(modifier)
    
    def get_score(self):
        score = 0
        time = Time_Manager.get_time()
        for i in range(len(self.modifiers) - 1, -1, -1):
            modifier = self.modifiers[i]
            if modifier.time_limit is None or time - modifier.start_time <= modifier.time_limit:
                change = getattr(modifier, "score_modifier")
                score += change
            else:
                #modifier is not active anymore
                self.modifiers.pop(i)  # Remove expired modifier
        return score

                    
        