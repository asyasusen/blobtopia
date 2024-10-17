from time_manager.time_manager import Time_Manager


class Stat_Modifier:
    def __init__(self, reason, time_limit=None, score_modifier=0):
        self.reason = reason
        self.time_limit = time_limit
        self.start_time = Time_Manager.get_time()
        self.friend_score_modifier= score_modifier