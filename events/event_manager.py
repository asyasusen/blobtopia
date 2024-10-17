class Event_Manager:
    current_events=[]
    future_events=[]
    @classmethod
    def add_event(cls, event):
        if event.wait_time==0:
            cls.current_events.append(event)
        else:
            cls.future_events.append(event)

    @classmethod
    def progress_current_events(cls):
        while len(cls.current_events)>0:
            x= cls.current_events[0]
            x.trigger()
            cls.current_events.pop(0)
            
    @classmethod
    def pass_days(cls, day): #should be only called by the time manager
        # Loop backwards over the indices of the list
        for i in range(len(cls.future_events) - 1, -1, -1):
            event = cls.future_events[i]
            event.wait_time -= day
            if event.wait_time <= 0:
                cls.current_events.append(event)
                cls.future_events.pop(i)  # Safely remove the item by index

