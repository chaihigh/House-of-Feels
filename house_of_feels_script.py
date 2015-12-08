from house_of_feels_classes import *
from house_of_feels_rooms import *
from house_of_feels_chars import *
from house_of_feels_obj import *

for room in house.rooms:
    for obj in obj_list:
        if obj.loc == room:
            room.obj.append(obj)
    for char in char_list:
        if char.loc == room:
            room.pers.append(char)

def check_inven(player):
    """Print the contents of the Player's inventory, and go into the options loop.

    Player -> None"""

    val = True
    print(player.check_inven())
        
    while True:

        if val == True:
            inven_str = ""
            for obj in player.inven:
                if inven_str == "":
                    inven_str += obj.name
                else:
                    inven_str += ", "+obj.name
            print("")
            print(" - ['examine OBJECT']"+" ( "+inven_str+" )")
            print(" - ['close backpack']")

        print("")
        inp = input()
        print("")

        val = "invalid"
            
        if inp.lower().startswith("examine"):
            val = True
            target = "lol"
            for obj in player.inven:
                if obj.name == inp[8:].lower().strip("."):
                    target = obj
                    if target not in player.inven:
                        val = "object not in inven"
            if target == "lol":
                val = "invalid examine target"
            if val == True:
                print(target.describe())
        if inp == "close backpack":
            val = True
            return ("You zip up your backpack.\n")
            break

        if val == "invalid":
            print("[not a valid command]")
        if val == "object not in inven":
            print("[that object is not in your inventory]")
        if val == "invalid examine target":
            print("[not a valid target]")


def go_deeper(go_deeper):
    """Go into the options loop for the given Go_Deeper.

    Go_Deeper -> None"""

    val = True
        
    while True:
            
        if val == True:
            trait_str = ""
            for obj in go_deeper.traits:
                if trait_str == "":
                    trait_str += obj.name
                else:
                    trait_str += ", "+obj.name
            print(" - ['examine OBJECT'] ( "+trait_str+" )")
            print(" - ['go back']")
            
        inp = input("\n")
        print("")

        val = "invalid"

        # If the command is to examine an object or trait...
        if inp.lower().startswith("examine"):
            target = "lol"
            val = True
            for obj in obj_list:
                if obj.name.lower() == inp[8:].lower().strip("."):
                    target = obj
                    if target not in go_deeper.traits:
                        val = "object not here"
            if target == "lol":
                val = "invalid target"
            if val == True:
                print(target.describe())
                print("")

        # If the command is to go back...
        if inp == "go back":
            break

        # If the command is invalid...
        if val == "invalid":
            print("not a valid command")
        if val == "object not here":
            print("that object is not here")
        if val == "invalid target":
            print("not a valid target")

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
            mads.loc = living_room
            print("You go back to the room you came from.")
            break

        if val == "invalid":
            print("not a valid command")

    return ""






######################
######MAIN##LOOP######
######################

val = True
print("""You stand before a house. Within this house... There are many dark and
painful things that lurk. If you choose to enter, you may never reemerge - and
if you do... you will not be the same.
""")
print("What do you want to do?")
while True:
    print("\n - ['enter']\n - ['turn back']\n")
    inp = input()
    print("")
    if inp.lower() == "turn back":
        print("""
A wise decision. You step away from the terrible house,
and flee the very sight of it.\n""")
        val = "turn back"
        break
    elif inp.lower() == "enter":
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
        print("[not a valid option]")


while True:

    if val == "turn back":
        break
    
    if val == True:
        
        # List all the valid options...
        for obj in obj_list:
            if obj.loc == "in_use":
                print(" - ['put away "+obj.name+"']")
        if mads.inven != []:
            print(" - ['check inventory']")
        room_str = ""
        room_list = []
        for room in mads.loc.adj:
            room_list.append(room)
        for room in mads.loc.inter:
            room_list.append(room)
        for room in room_list:
            if room_str == "":
                room_str += room.name
            else:
                room_str += ", "+room.name
        print(" - ['go to ROOM']"+" ( "+room_str+" )")
        if mads.loc.pers != []:
            char_str = ""
            for char in mads.loc.pers:
                if char_str == "":
                    char_str += char.name
                else:
                    char_str += ", "+char.name
            print(" - ['examine CHARACTER']"+" ( "+char_str+" )")
            print(" - ['talk to CHARACTER']")
        if mads.loc.obj != []:
            obj_str = ""
            for obj in mads.loc.obj:
                if obj_str == "":
                    obj_str += obj.name
                else:
                    obj_str += ", "+obj.name
            print(" - ['examine OBJECT']"+" ( "+obj_str+" )")
            for obj in mads.loc.obj:
                if obj.was_examined:
                    if obj.movable:
                        print(" - ['take "+obj.name+"']")
                        
    print("")
    inp = input()
    print("")

    val = "invalid"
        
    # If the command is to CHECK the inventory...
    if inp.lower().startswith("check"):
        val = True
        print(check_inven(mads))    

    # If the command is GO TO a room...
    if inp.lower().startswith("go to"):
        target_room = "lol"
        val = True
        for room in house.rooms:
            if room.name.lower() == inp[6:].lower().strip("."):
                target_room = room
        for room in mads.loc.inter:
            if room.name.lower() == inp[6:].lower().strip("."):
                target_room = room
        if target_room not in mads.loc.adj and target_room not in mads.loc.inter:
            val = "invalid room"
        if target_room == mads.loc:
            val = "already there"
        if val == True:
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
                print(go_deeper(target))

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
            print(target_pers.talk())

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
