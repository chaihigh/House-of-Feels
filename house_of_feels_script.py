from house_of_feels_classes import *
from house_of_feels_rooms import *
from house_of_feels_chars import *
from house_of_feels_obj import *

conditions = []

for room in house.rooms:
    for obj in obj_list:
        if obj.loc == room:
            room.obj.append(obj)
    for char in char_list:
        if char.loc == room:
            room.pers.append(char)
for openable in obj_list:
    for obj in obj_list:
        if obj.loc == openable:
            openable.objs.append(obj)

def check_inven(player):
    """Print the contents of the Player's inventory, and go into the
    options loop.

    Player -> None"""

    val = True
    print(player.check_inven())
        
    while True:

        if val == True:
            print("")
            if player.inven != []:
                inven_str = ""
                for obj in player.inven:
                    if inven_str == "":
                        inven_str += obj.name
                    else:
                        inven_str += ", "+obj.name
                print(" - ['examine OBJECT']"+" ( "+inven_str+" )")
                print(" - ['drop OBJECT']")
            print(" - ['close inventory']")

        print("")
        inp = input()
        print("")

        val = "invalid"
            
        if inp.lower().startswith("examine"):
            val = True
            target = "lol"
            for obj in player.inven:
                if obj.name == inp[8:].lower():
                    target = obj
                    if target not in player.inven:
                        val = "object not in inven"
            if target == "lol":
                val = "invalid examine target"
            if val == True:
                print(target.describe())
        if inp.lower().startswith("drop"):
            val = True
            target = "lol"
            for obj in player.inven:
                if obj.name == inp[5:].lower():
                    target = obj
                    if target not in player.inven:
                        val = "object not in inven"
            if target == "lol":
                val = "invalid examine target"
            if val == True:
                last_obj = False
                if len(player.inven) == 1:
                    last_obj = True
                player.inven.remove(target)
                player.loc.obj.append(target)
                target.loc = player.loc
                if last_obj == False:
                    print("You pull the "+target.name+" out of your backpack and drop it.")
                else:
                    print("You pull the "+target.name+" out of your backpack and drop it. "
                          +"Your backpack is empty.")
        if inp == "close inventory":
            val = True
            return ("You zip up your backpack.\n")
            break

        if val == "invalid":
            print("[not a valid command]")
        if val == "object not in inven":
            print("[that object is not in your inventory]")
        if val == "invalid examine target":
            print("[not a valid target]")


def action(go_deeper):
    """List the possible actions in the Go_Deeper.

    Go_Deeper -> string"""

    opt_str = ""

    # For all OPENABLES...
    if isinstance(go_deeper, Openable):
        if go_deeper.objs != "":
            for obj in go_deeper.objs:
                if obj.was_examined == True and go_deeper.can_examine == True:
                    opt_str += " - ['take "+obj.name+"']"
        if opt_str != "":
            opt_str += "\n"
        if go_deeper.is_open == False:
            opt_str += " - ['open "+go_deeper.name+"']"
        else:
            opt_str += " - ['close "+go_deeper.name+"']"
    
    # FRONT_DOOR actions...
    if go_deeper == front_door:
        if front_door.can_examine == True:
            opt_str += "\n - ['look through peephole']"
            if front_door_key in mads.inven:
                if front_door.is_locked == True:
                    opt_str += "\n - ['unlock with small key']"
                else:
                    opt_str += "\n - ['lock with small key']"

    return opt_str


def reaction(go_deeper, inp):
    """Carry out what the action causes.

    Go_Deeper, string -> None"""

    val = "invalid"

    # If the command is to TAKE an object...
    if inp.lower().startswith("take"):
        target_obj = "lol"
        val = True
        for obj in obj_list:
            if obj.name.lower() == inp[5:].lower().strip("."):
                target_obj = obj
                if target_obj not in go_deeper.objs:
                    val = "object not here"
        if target_obj.was_examined == False:
            val = "not examined"
        if target_obj == "lol":
            val = "invalid target"
        if val == True:
            mads.inven.append(target_obj)
            go_deeper.objs.remove(target_obj)
            target_obj.loc = "mads_inven"
            print("You take the "+target_obj.name+" and slip it in your backpack.\n")

    # FRONT_DOOR reactions...
    if go_deeper == front_door:
        if inp.lower() == "open front door":
            val = True
            if front_door.try_open() == True:
                front_door.try_open()
                front_door.can_examine = False
                front_door.desc = "It's open."
                print("You turn the handle and swing the door open.\n")
            else:
                print("You try to turn the handle, but it's locked.\n")
        if inp.lower() == "close front door":
            val = True
            front_door.close()
            front_door.can_examine = True
            front_door.desc = "It's closed. It has a peephole and a lock."
            print("You shut the door.\n")
        if inp.lower() == "look through peephole":
            val = True
            print("You peer through the peephole. It's cloudy out. There's "
                  +"no one around.\n")
        if inp.lower() == "lock with small key":
            val = True
            front_door.is_locked = True
            front_door_lock.desc = "It's locked."
            print("You fit the key into the lock and turn. The door clicks "
                  +"- it's locked.\n")
        if inp.lower() == "unlock with small key":
            val = True
            front_door.is_locked = False
            front_door_lock.desc = "It's unlocked."
            print("You fit the key into the lock and unlock the door.\n")

    # AIDANS_SINK_CAB reactions...
    if go_deeper == aidans_sink_cab:
        if inp.lower() == "open sink cabinet":
            val = True
            aidans_sink_cab.try_open()
            aidans_sink_cab.can_examine = True
            aidans_sink_cab.desc = "It's open."
            if aidans_sink_cab.objs != []:
                obj_str = ""
                objs_str = ""
                hid_str = ""
                hid_num = 0
                go_deeper_unhid_objs = []
                for obj in go_deeper.objs:
                    if (isinstance(obj, Hidden) and obj.was_revealed == True) \
                       or isinstance(obj, Hidden) == False:
                        go_deeper_unhid_objs.append(obj)
                    else:
                        hid_str += " "+obj.pre_reveal_desc
                for obj in go_deeper_unhid_objs:
                    #if isinstance(obj, Hidden) and obj.was_revealed == False:
                    #    obj_str = ""
                    #    hid_str += " "+obj.pre_reveal_desc
                    #else:
                    obj_str = obj.art+obj.name
                    if len(go_deeper_unhid_objs) == 1:
                        objs_str += obj_str
                    elif len(go_deeper_unhid_objs) == 2:
                        if obj == go_deeper_unhid_objs[-1]:
                            objs_str += " and "+obj_str
                        else:
                            objs_str += obj_str
                    else:
                        if obj == go_deeper_unhid_objs[-1]:
                            objs_str += "and "+obj_str
                        else:
                            objs_str += obj_str+", "
                print("You pull both handles and swing the cabinet doors open.\n"
                      +"Inside, you see "+objs_str+"."+hid_str+"\n")
            else:
                print("You pull both handles and swing the cabinet doors open."
                      +"It's empty.\n")
        if inp.lower() == "close sink cabinet":
            val = True
            aidans_sink_cab.close()
            aidans_sink_cab.can_examine = False
            aidans_sink_cab.desc = "It's a little beat up."
            print("You gently swing the doors shut.\n")

    return val

def go_deeper(go_deeper):
    """Go into the options loop for the given Go_Deeper.

    Go_Deeper -> None"""

    val = True
        
    while True:
            
        if val == True:
            if go_deeper.has_action == True:
                print(action(go_deeper))
            trait_str = ""
            for trait in go_deeper.traits:
                if trait_str == "":
                    trait_str += trait.name
                else:
                    trait_str += ", "+trait.name
            try:
                obj_str = ""
                for obj in go_deeper.objs:
                    if isinstance(obj, Hidden):
                        if obj.was_revealed == False:
                            if obj_str == "":
                                obj_str += obj.hid_name
                            else:
                                obj_str += ", "+obj.hid_name
                        else:
                            if obj_str == "":
                                obj_str += obj.name
                            else:
                                obj_str += ", "+obj.name
                    else:
                        if obj_str == "":
                            obj_str += obj.name
                        else:
                            obj_str += ", "+obj.name
                if go_deeper.can_examine == False:
                    print(" - ['examine OBJECT'] ( "+go_deeper.name+" )")
                else:
                    if trait_str != "" and obj_str != "":
                        examine_str = ", "+trait_str+", "+obj_str
                    elif trait_str != "" and obj_str == "":
                        examine_str = ", "+trait_str
                    elif trait_str == "" and obj_str != "":
                        examine_str = ", "+obj_str
                    else:
                        examine_str = ""
                    print(" - ['examine OBJECT'] ( "+go_deeper.name
                              +examine_str+" )")
            except:
                print(" - ['examine OBJECT'] ( "+go_deeper.name+", "+trait_str+" )")
            print(" - ['go back']")
            
        inp = input("\n")
        print("")

        val = "invalid"

        # If the command is a GO_DEEPER ACTION...
        if go_deeper.has_action == True:
            val = reaction(go_deeper, inp)

        # If the command is to EXAMINE an object or trait...
        if inp.lower().startswith("examine"):
            target = "lol"
            val = True
            if inp[8:].lower() == go_deeper.name:
                print(go_deeper.desc+"\n")
            else:
                for obj in obj_list:
                    if isinstance(obj, Hidden):
                        if obj.hid_name.lower() == inp[8:].lower():
                            target = obj
                    if obj.name.lower() == inp[8:].lower():
                        target = obj
                for trait in trait_list:
                    if trait.name.lower() == inp[8:].lower():
                        target = trait
                if target not in go_deeper.traits and target not in go_deeper.objs:
                    val = "invalid target"
                if target == "lol":
                    val = "invalid target"                        
                try:
                    if go_deeper.can_examine == False:
                        val = "invalid target"
                    else:
                        if val == True:
                            print(target.describe())
                            print("")                        
                except:
                    if val == True:
                        print(target.describe())
                        print("")

        # If the command is to GO BACK...
        if inp == "go back":
            break
        
        # If the command is INVALID...
        if val == "invalid":
            print("[not a valid command]")
        if val == "object not here":
            print("[that object is not here]")
        if val == "invalid target":
            print("[not a valid target]")
            
    return ("You turn away from the "+go_deeper.name+".\n")


def unlit(unlit):
    """Describe the Unlit Room, and go into the options loop.

    Unlit -> None"""

    print("It's dark - you can't see anything.\n")

    val = True

    while True:

        if mads.loc.is_lit == True:
            break
        
        if val == True:
            if mads.inven != []:
                print(" - ['check inventory']")
            if mads.loc.has_light_source == True:
                print(" - ['flip light switch']")
            if flashlight in mads.inven:
                print(" - ['use flashlight']")
            print(" - ['go back']")

        val = "invalid"

        inp = input("\n")
        print("")

        if inp == "check inventory":
            val = True
            print(check_inven(mads))
        
        if inp == "flip light switch":
            val = True
            mads.loc.can_describe = True
            mads.loc.is_lit = True
            print("Feeling around on the wall, you find a light switch and flip it on.")
            print("\nLight floods the room. "+mads.loc.desc)
            print(mads.loc.describe_contents())
            print(mads.loc.describe_rooms())
            break
        
        if inp == "use flashlight":
            val = True
            flashlight.turn_on()
            flashlight.loc = "in_use"
            mads.inven.remove(flashlight)
            print("You pull the flashlight out of your backpack and switch it on.")
            print("\nLight floods the room. "+mads.loc.desc)
            print(mads.loc.describe_contents())
            print(mads.loc.describe_rooms())
            break

        if inp == "go back":
            val = True
            mads.loc = mads.prev_loc
            print("You go back to the room you came from.\n")
            print(mads.loc.describe())
            break

        if val == "invalid":
            print("[not a valid command]")

    return ""






######################
######MAIN##LOOP######
######################

print("""You stand before a house. Within this house... There are many dark and
painful things that lurk. If you choose to enter, you may never reemerge - and
if you do... you will not be the same.
""")
print("What do you want to do?")

val = True

while True:
    if val == True:
        print("\n - ['enter']\n - ['turn back']\n")

    val = "invalid"
    
    inp = input()
    print("")
    
    if inp.lower() == "turn back":
        val = True
        print("""
A wise decision. You step away from the terrible house,
and flee the very sight of it.\n""")
        val = "turn back"
        break
    elif inp.lower() == "enter":
        val = True
        mads.loc = living_room
        print("""Very well.
As your hand closes on the door knob, a shudder runs down your spine.
Nonetheless, you swing the door open with a creak, and step over the threshold.
The door eases to a shut behind you of its own accord.
""")
        print(mads.loc.describe())
        print("")
        break
    else:
        val = "invalid"
    if val == "invalid":
        print("[not a valid command]\n")

val = True

while True:

    if val == "turn back":
        break
    
    if val == True:
        
        # List all the valid options...
        for obj in obj_list:
            if obj.loc == "in_use":
                print(" - ['put away "+obj.name+"']")
        for obj in mads.loc.obj:
            if obj.was_examined:
                if obj.movable:
                    print(" - ['take "+obj.name+"']")
        if mads.inven != []:
            print(" - ['check inventory']")
        if mads.loc.obj != []:
            obj_str = ""
            for obj in mads.loc.obj:
                if obj_str == "":
                    obj_str += obj.name
                else:
                    obj_str += ", "+obj.name
            print(" - ['examine OBJECT']"+" ( "+obj_str+" )")
        if mads.loc.pers != []:
            char_str = ""
            for char in mads.loc.pers:
                if char_str == "":
                    char_str += char.name
                else:
                    char_str += ", "+char.name
            print(" - ['examine CHARACTER']"+" ( "+char_str+" )")
            print(" - ['talk to CHARACTER']")
        room_str = ""
        room_list = []
        for room in mads.loc.adj:
            if room == landing and mads.loc == west_hall:
                room_list.append("second floor")
            elif room == west_hall and mads.loc == landing:
                room_list.append("first floor")
            else:
                room_list.append(room)
        for room in mads.loc.inter:
            room_list.append(room)
        for room in room_list:
            try:
                if room_str == "":
                    room_str += room.name
                else:
                    room_str += ", "+room.name
            except:
                if room_str == "":
                    room_str += room
                else:
                    room_str += ", "+room
                
        print(" - ['go to ROOM']"+" ( "+room_str+" )")


    print("")
    inp = input()
    print("")

    val = "invalid"

    # If the command is to TAKE an object...
    if inp.lower().startswith("take"):
        target_obj = "lol"
        val = True
        for obj in obj_list:
            if obj.name.lower() == inp[5:].lower().strip("."):
                target_obj = obj
                if target_obj not in mads.loc.obj:
                    val = "object not here"
        if target_obj.was_examined == False:
            val = "not examined"
        if target_obj.movable == False:
            val = "not movable"
        if target_obj == "lol":
            val = "invalid target"
        if val == True:
            mads.inven.append(target_obj)
            mads.loc.obj.remove(target_obj)
            target_obj.loc = "mads_inven"
            print("You take the "+target_obj.name+" and slip it in your backpack.\n")
    
    # If the command is to CHECK the inventory...
    if inp.lower().startswith("check"):
        val = True
        print(check_inven(mads))    

    # If the command is to EXAMINE an object or character...
    if inp.lower().startswith("examine"):
        target = "lol"
        val = True
        for obj in obj_list:
            if obj.name.lower() == inp[8:].lower().strip("."):
                target = obj
                if target not in mads.loc.obj:
                    val = "object not here"
        for pers in char_list:
            if pers.name.lower() == inp[8:].lower().strip("."):
                target = pers
                if target not in mads.loc.pers:
                    val = "person not here"
        if target == "lol":
            val = "invalid target"
        if val == True:
            if target.describe() != "go_deeper":
                print(target.describe())
                print("")
            else:
                print(target.desc+"\n")
                print(go_deeper(target))

    # If the command is to TALK to a character...
    if inp.lower().startswith("talk to"):
        val = True
        target_pers = "lol"
        for pers in char_list:
            if pers.name.lower() == inp[8:].lower().strip("."):
                target_pers = pers
                if target_pers not in mads.loc.pers:
                    val = "person not here"
        if target_pers == "lol":
            val = "invalid target"
        if val == True:
            target_pers.talk()
 
    # If the command is to PUT AWAY an object...
    if inp.lower().startswith("put away"):
        val = True
        target = "lol"
        for obj in obj_list:
            if obj.name.lower() == inp[9:].lower().strip("."):
                target = obj
                if target.loc != "in_use":
                    val = "invalid"
        if target == "lol":
            val = "invalid target"
        if val == True:
            target.loc = "mads_inven"
            mads.inven.append(target)
            if isinstance(target, On_or_Off):
                target.is_on = False
            print("You put the "+target.name+" back into your backpack.\n")
            if isinstance(mads.loc, Unlit):
                print(unlit(mads.loc))

    # If the command is GO TO a room...
    if inp.lower().startswith("go to"):
        target_room = "lol"
        val = True
        for room in house.rooms:
            if room.name.lower() == inp[6:].lower():
                target_room = room
        for room in mads.loc.inter:
            if room.name.lower() == inp[6:].lower():
                target_room = room
        if inp[6:].lower() == "second floor":
            target_room = landing
        if inp[6:].lower() == "first floor":
            target_room = west_hall
        if target_room not in mads.loc.adj and \
           target_room not in mads.loc.inter:
            val = "invalid room"
        if target_room == mads.loc:
            val = "already there"
        if val == True:
            mads.prev_loc = mads.loc
            mads.loc = target_room
            if isinstance(mads.loc, Unlit) == False:
                print(mads.loc.describe())
                print("")
            else:
                if mads.loc.is_lit == True:
                    print(mads.loc.describe())
                    print("")
                else:
                    if flashlight.is_on == True:
                        print(mads.loc.describe())
                        print("")
                    else:
                        print(unlit(mads.loc))
    
    # If an INVALID command was entered...
    if val != True:
        if val == "invalid":
            print("[not a valid command]")
        if val == "already there":
            print("[you are already in that room]")
        if val == "invalid room":
            print("[not a valid room]")
        if val == "person not here":
            print("[that person is not in this room]")
        if val == "object not here":
            print("[that object is not in this room]")
        if val == "invalid target":
            print("[not a valid target]")
        if val == "not examined":
            print("[you must examine that before you can take it]")
        if val == "not movable":
            print ("[you cannot take that object]")


