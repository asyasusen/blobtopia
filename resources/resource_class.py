from time_manager.time_manager import Time_Manager

class Resource:
    def __init__(self,name, supply=0, demand=0 ):
        self.name=name
        self.supply= supply
        self.demand= demand
    