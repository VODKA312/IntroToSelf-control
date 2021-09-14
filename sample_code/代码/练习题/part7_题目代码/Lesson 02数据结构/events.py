from random import randint

event_1 = """
date : 2018/01/24
time : 19:23.231
event name : Pedestrian Detected
event type : Observation
event code : 5-119-2
event id : h23-a19-mu8-994
"""

event_2 = """
date : 2018/01/24
time : 19:25.452
event name : Blocked Camera
event type : Observation
event code : 8-202-4
event id : h23-a19-mu8-995
additional_info: Front right camera blocked by unknown object
"""

event_3 = """
date : 2018/01/24
time : 19:25.512
event name : Pedestrian Occluded
event type : Observation
event code : 5-119-4
event id : h23-a19-mu8-996
additional_info: Occlusion due to sensor failure (camera: front right)
"""

event_4 = """
date : 2018/01/24
time : 19:25.720
event name : Emergency Stop
event type : Emergency Maneuver
event code : 8-000-4
event id : h23-a19-mu8-997
additional_info: Unacceptable uncertainty in pedestrian localization 
"""

random_event = """
date : 2018/01/24
time : 19:20.000
event name : example event
event type : example event type
event code : example code
event id : example id
"""

events_before = randint(200,300)
events_after = randint(200,300)

logged_events = [random_event for _ in range(events_before)] + [event_1, event_2, event_3, event_4] + [random_event for _ in range(events_after)]