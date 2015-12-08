from house_of_feels_rooms import *

# Living room objects...

# Movables...

key = Object("key", "It's a small, brass key.", "a ", living_room, True)
bottle = Object("bottle", "It's a clear plastic bottle.", "a ", living_room, True)
book = Object("book", "It's a small book, titled 'Jesus Calling'.", "a ", living_room, True)
umbrella = Object("umbrella", "It's a purple umbrella.", "an ", living_room, True)
flashlight = On_or_Off("flashlight", "It's a sleek, black flashlight.", "a ", living_room, True)

# Fixed's...

living_room_couch = Object("couch", "It's an old, beat-up leather couch.", "a ", living_room, False)

tv_stand = Object("TV stand", "It's a dark wooden TV stand.", "a ", living_room, False)

tv = Object("television", "It's a medium-sized, flatscreen TV.", "a ", living_room, False)

front_door = Go_Deeper("front door", "It has a peephole and a lock.", "the ", [], living_room, False)
peephole = Object("peephole", "It's a peephole.", "the ", front_door)
front_door_lock = Object("lock", "It's unlocked.", "the ", front_door)
front_door.traits = [peephole, front_door_lock]

obj_list = [key, bottle, book, umbrella, flashlight, living_room_couch, \
            tv_stand, tv, front_door, peephole, front_door_lock]
