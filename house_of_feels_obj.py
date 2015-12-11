from house_of_feels_rooms import *
from house_of_feels_traits import *

# -INDEX-

# -FIXED-
    # -LIVING ROOM-
    # -WEST HALLWAY-
    # -AIDAN'S BATH-
    # -BLACKWELL'S ROOM-

# -MOVABLE-
    # -ROOM-
        # -LIVING ROOM-
        # -NORTH HALLWAY-
        # -AIDAN'S BATH-
    # -OPENABLE-
        # -AIDANS_SINK_CAB-
        # -BLACKS_DECK-


# -FIXED- objects...


# In the -LIVING ROOM-...
living_room_couch = Object("couch", "It's an old, beat-up leather couch.", \
                           "a ", living_room)
tv_stand = Object("TV stand", "It's a dark wooden TV stand.", "a ", \
                  living_room)
tv = Object("television", "It's a medium-sized, flatscreen TV.", "a ", \
            living_room)
front_door = Lockable("front door", "It's closed. It has a peephole and a lock.", \
                      "the ", [peephole, front_door_lock], [], living_room, \
                      False, False, True, False, True)


# In the -WEST HALLWAY-...
photo = Go_Deeper("photo", "It's a nature shot. There's a tree on a hill, overlooking a lake.", \
                  "a ", [tree, lake], west_hall, False, False, False)


# In -AIDAN'S BATH-...
aidans_sink = Object("sink", "A slow but continuous drip falls from it.", "a ", aidans_bath)
aidans_sink_cab = Openable("sink cabinet", "It's a little beat up.", "the ", [], [], aidans_bath)
                           #False, False, True, False, False)

#In -BLACKWELL'S ROOM-...
blacks_desk = Openable("desk", "It's made of some dark wood, and looks polished. There's a drawer.", \
                       "a ", [], [], blacks_room)




# MOVABLE objects...


# Originating from a -ROOM-...

# From the -LIVING ROOM-...
front_door_key = Object("small key", "It's a small, brass key.", "a ", \
                        living_room, True)
bottle = Object("bottle", "It's a clear plastic bottle.", "a ", \
                living_room, True)
book = Object("book", "It's a small book, titled 'Jesus Calling'.", "a ", \
              living_room, True)
flashlight = On_or_Off("flashlight", "It's a sleek, black flashlight.", "a ", \
                       living_room, True)


# From the -NORTH HALLWAY-...
broom = Object("broom", "It's a broom.", "a ", north_hall, True)



# Originating from an -OPENABLE-...

# From -AIDANS_SINK_CAB-...
razor = Hidden("razor blade", "silver glint", "As you look closer, you notice some dried up flecks of brownish-red on the blade.", \
               "You pull at it until something pops out of the crack - a razor blade.", \
               "a ", "a ", "There's a silver glint wedged in a loose seam in the corner.", aidans_sink_cab, True)
shav_cream = Object("shaving cream", "It's half empty.", "a bottle of ", aidans_sink_cab, True)
hand_towel = Object("hand towel", "It's gray, and a little worn.", "a ", aidans_sink_cab, True)

# From -BLACKS_DESK-...
blacks_egun = On_or_Off("Blackwell's e-gun", "It's a little bulkier than a handgun. It's quite heavy.", \
                        "", blacks_desk, True)


obj_list = [front_door, living_room_couch, tv_stand, tv, photo, aidans_sink, \
            aidans_sink_cab, bottle, book, flashlight, front_door_key, razor, \
            broom, shav_cream, hand_towel, blacks_desk, blacks_egun]
