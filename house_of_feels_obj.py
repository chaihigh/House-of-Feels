from house_of_feels_rooms import *
from house_of_feels_traits import *



# Fixed's...


# In the living room...

living_room_couch = Object("couch", "It's an old, beat-up leather couch.", \
                           "a ", living_room)
tv_stand = Object("TV stand", "It's a dark wooden TV stand.", "a ", \
                  living_room)
tv = Object("television", "It's a medium-sized, flatscreen TV.", "a ", \
            living_room)
front_door = Lockable("front door", "It's closed. It has a peephole and a lock.", \
                      "the ", [peephole, front_door_lock], [], living_room, \
                      False, False, True, False, True)


# In the west hallway...

photo = Go_Deeper("photo", "It's a nature shot. There's a tree on a hill, overlooking a lake.", \
                  "a ", [tree, lake], west_hall, False, False, False)


# In Aidan's bath...

aidans_sink = Object("sink", "It's a sink.", "a ", aidans_bath)
aidans_sink_cab = Openable("sink cabinet", "It's a little beat up.", "the ", [], [], aidans_bath, \
                           False, False, True, False, False)




# Movables...


# Originating from a room...


# Originating from the living room...

front_door_key = Object("small key", "It's a small, brass key.", "a ", \
                        living_room, True)
bottle = Object("bottle", "It's a clear plastic bottle.", "a ", \
                living_room, True)
book = Object("book", "It's a small book, titled 'Jesus Calling'.", "a ", \
              living_room, True)
flashlight = On_or_Off("flashlight", "It's a sleek, black flashlight.", "a ", \
                       living_room, True)


# Originating from the north hallway...

broom = Object("broom", "It's a broom.", "a ", north_hall, True)


# Originating from an Openable...

razor = Hidden("razor blade", "silver glint", "It's a razor blade.", \
               "You pull at it until something pops out of the crack - a razor blade.", \
               "a ", "a ", "There's a silver glint wedged in a loose seam in the corner.", aidans_sink_cab, True)
shav_cream = Object("shaving cream", "It's half empty.", "a bottle of ", aidans_sink_cab, True)
hand_towel = Object("hand towel", "It's gray, and a little worn.", "a ", aidans_sink_cab, True)



obj_list = [front_door, living_room_couch, tv_stand, tv, photo, aidans_sink, \
            aidans_sink_cab, bottle, book, flashlight, front_door_key, razor, \
            broom, shav_cream, hand_towel]
