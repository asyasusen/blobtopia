from time_manager.time_manager import Time_Manager


class Relationship_Modifier:
    def __init__(self, reason, time_limit=None, friend_score_modifier=0, lover_score_modifier=0):
        self.reason = reason
        self.time_limit = time_limit
        self.start_time = Time_Manager.get_time()
        self.friend_score_modifier= friend_score_modifier
        self.lover_score_modifier = lover_score_modifier