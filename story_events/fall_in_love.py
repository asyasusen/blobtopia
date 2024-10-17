import random
from events.choice_class import Choice
from events.consequence_class import Consequence
from events.event_class import Event
from events.event_manager import Event_Manager
from relationship.relationship_manager import Relationship_Manager
from relationship.relationship_modifier_class import Relationship_Modifier
from time_manager.time_manager import Time_Manager


def fall_in_love_event(x, y):
    xtoy, ytox = Relationship_Manager.blobs_meet(x, y)
    # Define events and choices
    crush_event = Event("Love is in the Air", f"{x.name} has found themselves drawn to {y.name} in a way they can't ignore. What should they do with this budding affection?")
    got_over_crush_event = Event("Healing with Time", f"After some reflection, {x.name} realizes their feelings for {y.name} have started to fade.")

    tell_them = Choice("Share their feelings openly")
    forget_them = Choice("Let go of their feelings and move on")
    keep_in = Choice("Hold it close, keeping it a secret")

    # Add choices to events
    crush_event.add_choice(tell_them)
    crush_event.add_choice(keep_in)
    got_over_crush_event.add_choice(tell_them)
    got_over_crush_event.add_choice(forget_them)

    # Define consequences for the "tell them" choice
    if random.choice([True, False]):
        # Mutual crush outcome
        def mutual_crush_update():
            modf = Relationship_Modifier("mutual crush", friend_score_modifier=30, romance_score_modifier=50)
            xtoy.add_modifier(modf)
            ytox.add_modifier(modf)

        mutual_crush_consequences = [
            Consequence(effected_object=x, field="happiness", effect=30, text=f"To {x.name}'s delight, {y.name} feels the same way!"),
            Consequence(effected_object=y, field="happiness", effect=30, text=f"{y.name} is thrilled by {x.name}'s confession."),
            Consequence(func=mutual_crush_update)
        ]
        tell_them.add_consequence(mutual_crush_consequences)
    else:
        # Rejection outcome
        def rejection_update():
            xtoy.add_modifier(Relationship_Modifier("rejected their crush", friend_score_modifier=-10, romance_score_modifier=-20))
            ytox.add_modifier(Relationship_Modifier("platonically likes us", friend_score_modifier=-30, romance_score_modifier=-30))

        rejection_consequences = [
            Consequence(effected_object=x, field="happiness", effect=-50, text=f"With a heavy heart, {x.name} faces rejection as {y.name} gently turns them down."),
            Consequence(func=rejection_update)
        ]
        tell_them.add_consequence(rejection_consequences)

    # Define consequences for the "keep it inside" choice
    def keep_inside_func():
        got_over_crush_event.wait_time = 2
        Event_Manager.add_event(got_over_crush_event)

    keep_in_consequences = [
        Consequence(effected_object=x, field="happiness", effect=-10, text=f"The weight of unspoken words lingers, tugging at {x.name}'s heart."),
        Consequence(func=keep_inside_func)
    ]
    keep_in.add_consequence(keep_in_consequences)

    # Define consequences for the "forget them" choice
    forget_them.add_consequence(Consequence(effected_object=x, field="happiness", effect=10, text="With a new sense of clarity, {x.name} feels lighter as they decide to move on."))

    # Add events to the Event Manager
    Event_Manager.add_event(crush_event)

    # Simulate event progression
    for i in range(10):
        Event_Manager.progress_current_events()
        Time_Manager.pass_days()

