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

# -INDEX-

# -CHECK_INVEN-
# -GET_CONTENTS_STR-
# -GO_DEEPER ACTION-
    # -OPENABLE ACTIONS-
    # -FRONT_DOOR ACTIONS-
# -GO_DEEPER REACTION-
    # -GO_DEEPER TAKE-
    # -FRONT_DOOR REACTIONS-
    # -AIDANS_SINK_CAB REACTIONS-
    # -BLACKS_DESK REACTIONS-
# -GO_DEEPER-
    # -HAS ACTION-
    # -GO_DEEPER EXAMINE-
    # -GO_DEEPER GO BACK-
    # -GO_DEEPER INVALID-
# -UNLIT-
    # -UNLIT ACTIONS-
    # -UNLIT CHECK-
    # -USE FLASHLIGHT-
    # -FLIP LIGHT SWITCH-
    # -UNLIT GO BACK-
    # -UNLIT INVALID-
# -ENTRY LOOP-
# -MAIN LOOP-
    # -MAIN ACTIONS-
    # -PUT AWAY-
    # -TAKE-
    # -MAIN CHECK-
    # -MAIN EXAMINE-
    # -TALK-
    # -GO TO-
    # -INVALID-

        
# To enter the -CHECK_INVEN- loop...
def check_inven(player, loop):
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
                if loop != "go_deeper":
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
        if inp.lower().startswith("drop") and loop != "go_deeper":
            val = True
            target = "lol"
            for obj in player.inven:
                if obj.name.lower() == inp[5:].lower():
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
                    if target.name[0].isupper():
                        print("You pull "+target.name+" out of your backpack and drop it.")
                    else:
                        print("You pull the "+target.name+" out of your backpack and drop it.")
                else:
                    if target.name[0].isupper():
                        print("You pull "+target.name+" out of your backpack and drop it. "
                              +"Your backpack is empty.")
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

# -GET-UNHID_EXT_OBJS-...
def get_unhid_ext_objs(openable):
    """Determine if there are any external Objects in an Openable
    that are unhidden.

    Openable -> boolean"""

    unhid_ext_objs = []
    
    for obj in openable.objs:
        if obj.is_external == True:
            if isinstance(obj, Hidden_Object) == False:
                unhid_ext_objs.append(obj)
            else:
                if obj.was_revealed == True:
                    unhid_ext_objs.append(obj)

    return unhid_ext_objs


# -GET_UNHID_INT_OBJS-...
def get_unhid_int_objs(openable):
    """Determine if there are any internal Objects in an Openable
    that are unhidden.

    Openable -> boolean"""

    unhid_int_objs = []
    
    for obj in openable.objs:
        if obj.is_external == False:
            if isinstance(obj, Hidden_Object) == False:
                unhid_int_objs.append(obj)
            else:
                if obj.was_revealed == True:
                    unhid_int_objs.append(obj)

    return unhid_int_objs


# -GET_EXT_TRAITS-...
def get_ext_traits(go_deeper):
    """Take a Go_Deeper and return a string describing the Go_Deeper's external
    traits and a string listing its external traits.

    Go_Deeper -> string"""

    ext_traits_desc_str = ""
    ext_traits_list_str = ""

    for trait in go_deeper.traits:
        if trait.is_external == True:
            if isinstance(trait, Hidden_Trait):
                if trait.was_revealed == False:
                    ext_traits_desc_str += trait.pre_reveal_desc
                    ext_traits_list_str += ", "+trait.hid_name
                else:
                    ext_traits_desc_str += trait.post_reveal_desc
                    ext_traits_list_str += ", "+trait.name
            else:
                ext_traits_desc_str += trait.non_hid_desc
                ext_traits_list_str += ", "+trait.name

    return (ext_traits_desc_str, ext_traits_list_str)

# -GET_INT_TRAITS-...
def get_int_traits(go_deeper):
    """Take a Go_Deeper and return a string describing the Go_Deeper's internal
    traits and a string listing its internal traits.

    Go_Deeper -> string"""

    int_traits_desc_str = ""
    int_traits_list_str = ""

    for trait in go_deeper.traits:
        if trait.is_external == False:
            if isinstance(trait, Hidden_Trait):
                if trait.was_revealed == False:
                    int_traits_desc_str += trait.pre_reveal_desc
                    int_traits_list_str += ", "+trait.hid_name
                else:
                    int_traits_desc_str += trait.post_reveal_desc
                    int_traits_list_str += ", "+trait.name
            else:
                int_traits_desc_str += trait.non_hid_desc
                int_traits_list_str += ", "+trait.name

    return (int_traits_desc_str, int_traits_list_str)


# To -GET_EXT_CONTENTS- for the contents of an Openable...
def get_ext_contents(openable):
    """wrongTake an Openable and return a string of all unhidden objects,
    and a hidden object description string, both in one 'contents' string.

    Openable -> string"""

    ext_objs_desc_str = ""
    hid_ext_objs_desc_str = ""
    ext_objs_list_str = ""
    openable_unhid_ext_objs = []

    for obj in openable.objs:
        if obj.is_external == True:
            if (isinstance(obj, Hidden_Object) and obj.was_revealed == True) \
               or isinstance(obj, Hidden_Object) == False:
                openable_unhid_ext_objs.append(obj)
            else:
                hid_ext_objs_desc_str += obj.pre_reveal_desc
                ext_objs_list_str += ", "+obj.hid_name

    for obj in openable_unhid_ext_objs:
        ext_objs_list_str += ", "+obj.name
        if len(openable_unhid_ext_objs) == 1:
            ext_objs_desc_str += obj.art+obj.name+"."
        elif len(openable_unhid_ext_objs) == 2:
            if obj == openable_unhid_ext_objs[-1]:
                ext_objs_desc_str += " and "+obj.art+obj.name+"."
            else:
                ext_objs_desc_str += obj.art+obj.name
        else:
            if obj == openable_unhid_ext_objs[-1]:
                ext_objs_desc_str += "and "+obj.art+obj.name+"."
            else:
                ext_objs_desc_str += obj.art+obj.name+", "

    return (ext_objs_desc_str+hid_ext_objs_desc_str+get_ext_traits(openable)[0], \
            ext_objs_list_str+get_ext_traits(openable)[1])


# To -GET_INT_CONTENTS- for the contents of an Openable...
def get_int_contents(openable):
    """Take an Openable and return a string of all unhidden objects,
    and a hidden object description string, both in one 'contents' string.

    Openable -> string"""

    int_objs_desc_str = ""
    hid_int_objs_desc_str = ""
    int_objs_list_str = ""
    openable_unhid_int_objs = []

    for obj in openable.objs:
        if obj.is_external == False:
            if (isinstance(obj, Hidden_Object) and obj.was_revealed == True) \
               or isinstance(obj, Hidden_Object) == False:
                openable_unhid_int_objs.append(obj)
            else:
                hid_int_objs_desc_str += obj.pre_reveal_desc
                int_objs_list_str += ", "+obj.hid_name

    for obj in openable_unhid_int_objs:
        int_objs_list_str += ", "+obj.name
        if len(openable_unhid_int_objs) == 1:
            int_objs_desc_str += obj.art+obj.name+"."
        elif len(openable_unhid_int_objs) == 2:
            if obj == openable_unhid_int_objs[-1]:
                int_objs_desc_str += " and "+obj.art+obj.name+"."
            else:
                int_objs_desc_str += obj.art+obj.name
        else:
            if obj == openable_unhid_int_objs[-1]:
                int_objs_desc_str += "and "+obj.art+obj.name+"."
            else:
                int_objs_desc_str += obj.art+obj.name+", "

    return (int_objs_desc_str+hid_int_objs_desc_str+get_int_traits(openable)[0], \
            int_objs_list_str+get_int_traits(openable)[1])


# -LOCKABLE_ACTIONS-...
def lockable_actions(lockable):
    """List command to lock a Lockable.

    Lockable -> string"""

    opt_str = ""

    if lockable == front_door:
        key = front_door_key

    if key in mads.inven:
        if lockable.is_open == False:
            if lockable.is_locked == True:
                opt_str += "\n - ['unlock with "+key.name+"']"
            else:
                opt_str += "\n - ['lock with "+key.name+"']"

    return opt_str


# -LOCKABLE_REACTIONS-...
def lockable_reactions(lockable, inp):
    """Carry out a command for a Lockable.

    Lockable -> val"""

    val = "invalid"

    if lockable == front_door:
        key = front_door_key

    if inp.lower().startswith("lock with"):
        val = True
        if key.name.lower() == inp[10:].lower() and lockable.is_open == False and \
           lockable.is_locked == False:
            lockable.lock()
            print("You fit the key in the lock and turn - it's locked.\n")
        else:
            val = "invalid"
    if inp.lower().startswith("unlock with"):
        val = True
        if key.name.lower() == inp[12:].lower() and lockable.is_open == False and \
           lockable.is_locked == True:
            lockable.unlock()
            print("You fit the key in the lock and turn - it's unlocked.\n")
        else:
            val = "invalid"

    return val


# -OPENABLE_ACTIONS-...
def openable_actions(openable):
    """List possible commands for an Openable and carry out those commands.

    Openable -> None"""

    opt_str = ""

    # List all common -OPENABLE ACTIONS-...
    if openable.objs != "":
        for obj in openable.objs:
            if obj.was_examined == True and \
               openable.can_examine_contents == "int" and \
               obj.is_external == False:
                opt_str += " - ['take "+obj.name+"']\n"
        for obj in openable.objs:
            if obj.was_examined == True and \
               openable.can_examine_contents == "ext" and \
                obj.is_external == True:
                opt_str += " - ['take "+obj.name+"']\n"
    if openable.is_open == False:
        opt_str += " - ['open "+openable.name+"']"
    else:
        opt_str += " - ['close "+openable.name+"']"

    if isinstance(openable, Lockable):
        opt_str += lockable_actions(openable)

    if openable.can_examine_contents == "ext":
        opt_str += "\n - ['examine OBJECT'] ( "+openable.name+get_ext_contents(openable)[1]+" )"
    else:
        opt_str += "\n - ['examine OBJECT'] ( "+openable.name+get_int_contents(openable)[1]+" )"

    return opt_str

# Carry out -OPENABLE REACTIONS-...
def openable_reactions(openable, inp):
    """Carry out commands specific to Openables.

    Openable -> None"""

    val = "invalid"

    if isinstance(openable, Lockable):
        val = lockable_reactions(openable, inp)

    # If the command is to -OPENABLE TAKE- an object...
    if inp.lower().startswith("take"):
        target = "lol"
        val = True
        for obj in obj_list:
            if obj.name.lower() == inp[5:].lower().strip("."):
                target = obj
                if target not in openable.objs:
                    val = "invalid target"
        if isinstance(target, Object) or isinstance(target, Hidden_Object):
            if target.was_examined == False:
                val = "not examined"
        if target == "lol":
            val = "invalid target"
        if val == True:
            mads.inven.append(target)
            openable.objs.remove(target)
            target.loc = "mads_inven"
            if target.name[0].isupper():
                print("You take "+target.name+" and slip it in your backpack.\n")
            else:
                print("You take the "+target.name+" and slip it in your backpack.\n")

    # If the command is to -OPENABLE EXAMINE- an object or trait...
    if inp.lower().startswith("examine"):
        target = "lol"
        val = True
        openable_unhid_ext_objs = []
        openable_unhid_int_objs = []
        for obj in openable.objs:
            if isinstance(obj, Hidden_Object):
                if obj.was_revealed:
                    if obj.is_external:
                        openable_unhid_ext_objs.append(obj)
                    else:
                        openable_unhid_int_objs.append(obj)
            else:
                if obj.is_external:
                    openable_unhid_ext_objs.append(obj)
                else:
                    openable_unhid_int_objs.append(obj)

        if openable.name.lower() == inp[8:].lower():
            target = openable
            if openable.can_examine_contents == "ext":
                if get_ext_contents(openable)[0] != "":
                    if openable_unhid_ext_objs != []:
                        print(openable.describe()+" On the "+openable.name+", you see "
                              +get_ext_contents(openable)[0]+"\n")
                    else:
                        print(openable.describe()+get_ext_contents(openable)[0]+"\n")
                else:
                    print(openable.describe()+"\n")
            else:
                if get_int_contents(openable)[0] != "":
                    if openable_unhid_int_objs != []:
                        print(openable.describe()+" Inside, you see "
                              +get_int_contents(openable)[0]+"\n")
                    else:
                        print(openable.describe()+get_int_contents(openable)[0]+"\n")                
                else:
                    print(openable.describe()+" It's empty.\n")
        else:
            for obj in openable.objs:
                if isinstance(obj, Hidden_Object):
                    if obj.was_revealed == False:
                        if openable.can_examine_contents == "ext" and \
                           obj.is_external == True:
                            if obj.hid_name.lower() == inp[8:].lower():
                                target = obj
                        if openable.can_examine_contents == "int" and \
                           obj.is_external == False:
                            if obj.hid_name.lower() == inp[8:].lower():
                                target = obj
                    else:
                        if openable.can_examine_contents == "ext" and \
                           obj.is_external == True:
                            if obj.name.lower() == inp[8:].lower():
                                target = obj
                        if openable.can_examine_contents == "int" and \
                           obj.is_external == False:
                            if obj.name.lower() == inp[8:].lower():
                                target = obj
                else:
                    if openable.can_examine_contents == "ext" and \
                       obj.is_external == True:
                        if obj.name.lower() == inp[8:].lower():
                            target = obj
                    if openable.can_examine_contents == "int" and \
                       obj.is_external == False:
                        if obj.name.lower() == inp[8:].lower():
                            target = obj
            for trait in openable.traits:
                if isinstance(trait, Hidden_Trait):
                    if trait.was_revealed == False:
                        if openable.can_examine_contents == "ext" and \
                           trait.is_external == True:
                            if trait.hid_name.lower() == inp[8:].lower():
                                target = trait
                        if openable.can_examine_contents == "int" and \
                           trait.is_external == False:
                            if trait.hid_name.lower() == inp[8:].lower():
                                target = trait
                    else:
                        if openable.can_examine_contents == "ext" and \
                           trait.is_external == True:
                            if trait.name.lower() == inp[8:].lower():
                                target = trait
                        if openable.can_examine_contents == "int" and \
                           trait.is_external == False:
                            if trait.name.lower() == inp[8:].lower():
                                target = trait
                else:
                    if openable.can_examine_contents == "ext" and \
                       trait.is_external == True:
                        if trait.name.lower() == inp[8:].lower():
                            target = trait
                    if openable.can_examine_contents == "int" and \
                       trait.is_external == False:
                        if trait.name.lower() == inp[8:].lower():
                            target = trait
            if target == "lol":
                val = "invalid target"
            if val == True:
                print(target.describe()+"\n")

    # Carry out -FRONT_DOOR REACTIONS-...
    if openable == front_door:
        if inp.lower() == "open front door":
            val = True
            if front_door.try_open() == True:
                front_door.try_open()
                front_door.can_examine_contents = "int"
                print("You turn the handle and swing the door open.\n")
            else:
                print("You try to turn the handle, but it's locked.\n")
        if inp.lower() == "close front door":
            val = True
            front_door.close()
            front_door.can_examine_contents = "ext"
            print("You shut the door.\n")


    # Carry out -COMMON OPENABLE-WITH-CONTENTS REACTIONS-...
    if openable == aidans_sink_cab or openable == blacks_desk:
        if inp.lower() == "open "+openable.name:
            val = True
            openable.try_open()
            openable.can_examine_contents = "int"
            if get_int_contents(openable)[0] != "":
                if get_unhid_int_objs(openable) != []:
                    if openable == aidans_sink_cab:
                        print("You pull both handles and swing the cabinet doors open.\n\n"
                              +"Inside, you see "+get_int_contents(aidans_sink_cab)[0]+"\n")
                    if openable == blacks_desk:
                        print("You pull the handle of the drawer and slide it open.\n\n"
                              +"Inside, you see "+get_int_contents(blacks_desk)[0]+"\n")
                else:
                    if openable == aidans_sink_cab:
                        print("You pull both handles and swing the cabinet doors open.\n\n"+get_int_contents(aidans_sink_cab)[0]+"\n")
                    if openable == blacks_desk:
                        print("You pull the handle of the drawer and slide it open.\n\n"+get_int_contents(blacks_desk)[0]+"\n")
            else:
                if openable == aidans_sink_cab:
                    print("You pull both handles and swing the cabinet doors open. It's empty.\n")
                if openable == blacks_desk:
                    print("You pull the handle of the drawer and slide it open. It's empty.\n")
        if inp.lower() == "close "+openable.name:
            val = True
            openable.close()
            openable.can_examine_contents = "ext"
            if openable == aidans_sink_cab:
                print("You gently swing the doors shut.\n")
            if openable == blacks_desk:
                print("You push the drawer shut with a muffled click.\n")

    return val


# Generate each possible -GO_DEEPER ACTION-...
def go_deeper_actions(go_deeper):
    """List the possible actions in the Go_Deeper.

    Go_Deeper -> string"""

    opt_str = ""
    
    # List -FRONT_DOOR ACTIONS-...
    if go_deeper == front_door:
        if front_door.can_examine_contents == "ext":
            opt_str += " - ['look through peephole']"

    # List -BLACKS_DESK ACTIONS-...
    if go_deeper == blacks_desk:
        opt_str += " - ['touch desk']"

    # List -PHOTO ACTIONS-...
    if go_deeper == photo:
        opt_str += " - ['touch photo']"

    return opt_str


# Carry out a -GO_DEEPER REACTION-...
def go_deeper_reactions(go_deeper, inp):
    """Carry out what the action causes.

    Go_Deeper, string -> None"""

    val = "invalid"

    # Carry out -PHOTO REACTIONS-...
    if go_deeper == photo:
        if inp.lower() == "touch photo":
            val = True
            print("You touch the photo.\n")

    # Carry out -BLACKS_DESK REACTIONS-...
    if go_deeper == blacks_desk:
        if inp.lower() == "touch desk":
            val = True
            print("You touch the desk.\n")

    # Carry out -FRONT_DOOR REACTIONS-...
    if go_deeper == front_door:
        if inp.lower() == "look through peephole" and \
           front_door.can_examine_contents == "ext":
            val = True
            print("You peer through the peephole. It's cloudy out. There's "
                  +"no one around.\n")                    

    return val


# To enter the -GO_DEEPER- options loop...
def go_deeper(go_deeper):
    """Go into the options loop for the given Go_Deeper.

    Go_Deeper -> None"""

    if isinstance(go_deeper, Openable) == False:
        print(go_deeper.describe()+get_ext_traits(go_deeper)[0])
        if get_ext_traits(go_deeper)[0] != "":
            print("")
    else:
        if go_deeper.can_examine_contents == "ext":
            if get_unhid_ext_objs(go_deeper) != []:
                print(go_deeper.describe()+" On the "+go_deeper.name+", you see "
                      +get_ext_contents(go_deeper)[0]+"\n")
            else:
                print(go_deeper.describe()+get_ext_contents(go_deeper)[0]+"\n")
        else:
            if get_unhid_int_objs(go_deeper) != []:
                print(go_deeper.describe()+" Inside, you see "
                      +get_int_contents(go_deeper)[0]+"\n")
            else:
                print(go_deeper.describe()+get_int_contents(go_deeper)[0]+"\n")                

    val = True

    while True:
        
        if val == True:

            if mads.inven != []:
                print(" - ['check inventory']")

            if go_deeper.has_action == True:
                if go_deeper_actions(go_deeper) != "":
                    print(go_deeper_actions(go_deeper))
            if isinstance(go_deeper, Openable):
                print(openable_actions(go_deeper))
            else:
                print(" - ['examine OBJECT'] ( "+go_deeper.name+get_ext_traits(go_deeper)[1]+" )")
            print(" - ['go back']")
            
        inp = input("\n")
        print("")

        val = "invalid"

        # If the command is to -GO_DEEPER CHECK_INVEN-...
        if inp.lower() == "check inventory":
            val = True
            print(check_inven(mads, "go_deeper"))
        else:
            
            # If the command is for a Go_Deeper that -HAS ACTION-...
            if go_deeper.has_action == True:
                val = go_deeper_reactions(go_deeper, inp)
            if val != True:
                if isinstance(go_deeper, Openable):
                    val = openable_reactions(go_deeper, inp)
            
        # If the command is to -GO_DEEPER EXAMINE- an object or trait...
        if isinstance(go_deeper, Openable) == False:
            if inp.lower().startswith("examine"):
                target = "lol"
                val = True
                if inp[8:].lower() == go_deeper.name:
                    print(go_deeper.describe()+get_ext_traits(go_deeper)[0]+"\n")
                else:
                    for trait in go_deeper.traits:
                        if isinstance(trait, Hidden_Trait) and \
                            trait.hid_name.lower() == inp[8:].lower():
                            if trait.was_revealed == False:
                                target = trait
                        elif isinstance(trait, Hidden_Trait) and \
                           trait.name.lower() == inp[8:].lower():
                            if trait.was_revealed == True:
                                target = trait
                        else:
                            if trait.name.lower() == inp[8:].lower():
                                target = trait
                    if target == "lol":
                        val = "invalid target"                        
                    if val == True:
                        print(target.describe())
                        print("")

        # If the command is to -GO_DEEPER GO BACK-...
        if inp == "go back":
            break
        
        # If the command is -GO_DEEPER INVALID-...
        if val == "invalid":
            print("[not a valid command]")
        if val == "invalid target":
            print("[not a valid target]")
        if val == "not examined":
            print("[you must examine that before you can take it]")
            
    return ("You turn away from the "+go_deeper.name+".\n")


# To enter the -UNLIT- options loop...
def unlit(unlit):
    """Describe the Unlit Room, and go into the options loop.

    Unlit -> None"""

    print("It's dark - you can't see anything.\n")

    val = True

    while True:

        if mads.loc.is_lit == True:
            break

        # List -UNLIT ACTIONS-...
        if val == True:
            if mads.inven != []:
                print(" - ['check inventory']")
            if flashlight in mads.inven:
                print(" - ['use flashlight']")
            if mads.loc.has_light_source == True:
                print(" - ['flip light switch']")
            print(" - ['go back']")

        val = "invalid"

        inp = input("\n")
        print("")

        # If the command is to -UNLIT CHECK- the inventory-
        if inp == "check inventory":
            val = True
            print(check_inven(mads, "unlit"))

        # If the command is to -USE FLASHLIGHT-...
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

        # If the command is to -FLIP LIGHT SWITCH-...
        if inp == "flip light switch":
            val = True
            mads.loc.can_describe = True
            mads.loc.is_lit = True
            print("Feeling around on the wall, you find a light switch and flip it on.")
            print("\nLight floods the room. "+mads.loc.desc)
            print(mads.loc.describe_contents())
            print(mads.loc.describe_rooms())
            break

        # If the command is to -UNLIT GO BACK-...
        if inp == "go back":
            val = True
            mads.loc = mads.prev_loc
            print("You go back to the room you came from.\n")
            print(mads.loc.describe())
            break

        # If the command is -UNLIT INVALID-...
        if val == "invalid":
            print("[not a valid command]")

    return ""







# The -ENTRY LOOP- of the game...
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

# The -MAIN LOOP- of the game...
while True:

    if val == "turn back":
        break
    
    if val == True:
        
        # List all the valid -MAIN ACTIONS-...
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

    # If the command is to -PUT AWAY- an object...
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

    # If the command is to -MAIN TAKE- an object...
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
    
    # If the command is to -MAIN CHECK- the inventory...
    if inp.lower().startswith("check"):
        val = True
        print(check_inven(mads, "main"))    

    # If the command is to -MAIN EXAMINE- an object or character...
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
            if isinstance(target, Go_Deeper):
                print(go_deeper(target))
            else:
                print(target.describe()+"\n")

    # If the command is to -TALK- to a character...
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
 
    # If the command is -GO TO- a room...
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
    
    # If the command is -MAIN INVALID-...
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


