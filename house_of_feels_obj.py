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
front_door = Lockable("front door", "It's closed, but unlocked.", \
                      "It's open.", "It's closed, but unlocked.", \
                      "It's locked.", "the ", [peephole], [], living_room, \
                      False, False, False, True, False, "ext", False)


# In the -WEST HALLWAY-...
photo = Go_Deeper("photo", "It's a nature shot.", \
                  "a ", [tree, lake, bird], west_hall, False, False, False, True)


# In -AIDAN'S BATH-...
aidans_sink = Object("sink", "A slow but continuous drip falls from it.", "a ", aidans_bath)
aidans_sink_cab = Openable("sink cabinet", "It's a little beat up.", "The doors are hanging open.", "It's a little beat up.", "the ", [], [], aidans_bath)

#In -BLACKWELL'S ROOM-...
blacks_desk = Openable("desk", "It's made of some dark wood, and looks polished. There's a drawer.", \
                       "It's made of some dark wood, and looks polished. The drawer is hanging open.", \
                       "It's made of some dark wood, and looks polished. There's a drawer.", "a ", [staple, stain, smiley_face, sticky_note], [], blacks_room, False, False, False, True)




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
razor = Hidden_Object("razor blade", "silver glint", "As you look closer, you notice some dried up flecks of brownish-red on the blade.", \
               "You pull at it until something pops out of the crack - a razor blade.", \
               "a ", "a ", " There's a silver glint wedged in a loose seam in the corner.", aidans_sink_cab, True)
shav_cream = Object("shaving cream", "It's half empty.", "a bottle of ", aidans_sink_cab, True)
hand_towel = Object("hand towel", "It's gray, and a little worn.", "a ", aidans_sink_cab, True)

# From -BLACKS_DESK-...
blacks_egun = On_or_Off("Blackwell's e-gun", "It's a little bulkier than a handgun. It's quite heavy.", \
                        "", blacks_desk, True)
note_pad = Object("note pad", "Something is written on it in an elegant scrawl.", "a ", blacks_desk, True, False, True)
receipt = Hidden_Object("receipt", "crumpled wad", "It's from a coffee shop, for a bagel and an iced tea.", \
                 "You smooth out the paper and see that it's a receipt.", "a ", "a ", " There's a crumpled wad on the desk.", \
                 blacks_desk, True, False, False, True)
penny = Hidden_Object("penny", "copper thing", "It's shiny.", "You look closer - it's a penny.", "a ", "a ", \
                      " Something copper in a corner of the drawer catches your eye.", blacks_desk, True, \
                      False, False, False)

obj_list = [front_door, living_room_couch, tv_stand, tv, photo, aidans_sink, \
            aidans_sink_cab, bottle, book, flashlight, front_door_key, razor, \
            broom, shav_cream, hand_towel, blacks_desk, blacks_egun, note_pad, \
            receipt, penny]
