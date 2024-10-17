
from time_manager.time_manager import Time_Manager


class Stat_Manager:

    stat_names_list = []
    stat_list = []



    
    @classmethod
    def add_stat_to_object(cls, object, stat):
        from stats.stat_of_object_class import Stat_Of_Object
        stat_to_add = cls.__stat_string_or_object_give_object__(stat)
        cls.__check_if_object_has_stats__(stat, object)
        for item in object.stats:
            if item.stat_name== stat_to_add.stat_name:
                return item
        return Stat_Of_Object(object, stat)
    
    @classmethod
    def get_stat_of_object(cls, object, stat):
        stat_to_check = cls.__stat_string_or_object_give_object__(stat)
        cls.__check_if_object_has_stats__( object)
        None
        for item in object.stats:
            if item.stat_name == stat_to_check.stat_name:
                return item
        return
    
    @classmethod
    def create_get_stat_of_object(cls, object, stat):
        from stats.stat_of_object_class import Stat_Of_Object
        stat_gotten = cls.get_stat_of_object(object, stat)
        if stat_gotten is None:
            stat_gotten = Stat_Of_Object(object, stat)
        return stat_gotten
    
    @classmethod
    def add_modifier_to_stat_of_object(cls, object, stat, modifier):
        """creates stat if it doesn't exist"""
        stat_of_object = cls.create_get_stat_of_object( object, stat)
        stat_of_object.add_modifier(modifier)

    @classmethod
    def __create_get_stat__(cls, name):
        """Creates a new stat that can be used on any object"""
        if cls.__is_stat_name_used__(name):
            index = cls.stat_names_list.index(name)
            return cls.stat_list[index]
        else:
            return Stat_Manager(name)
        

    def __init__(self, stat_name):
        if self.__is_stat_name_used__(stat_name):
            raise ValueError(f"stat name {stat_name} already exists")
        self.stat_name = stat_name
        self.stat_names_list.append(stat_name)
        self.stat_list.append(self)

    @classmethod
    def __is_stat_name_used__(cls,name):                    
        return name in cls.stat_names_list

    @classmethod
    def __stat_string_or_object_give_object__(cls, stat):
        if isinstance(stat, str):
            return cls.__create_get_stat__(stat)
        elif isinstance(stat, Stat_Manager):
            return stat
        else:
            raise ValueError(f"Stat should be either string or instance of Stat_Manager class.")
    
    @classmethod
    def __check_if_object_has_stats__(cls, object):
        if not hasattr(object, "stats"):
            raise ValueError("Object doesn't have stats array.")
        
