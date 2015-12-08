from house_of_feels import *


lol_place = Room("lol", "cause I can")
lol_obj = Object("lol", "cause I can", "a", lol_place)

porch = Room("the porch", "it's a porch")
mads = Player("Madison", "You're oblivious to the pain you are about to experience", porch)

entry = Room("the entryway", "the goddam entryway, figure it out")
lucys_room = Room("Lucy's room", "idk atm", [], [], [])
levis_room = Room("Levi's room", "dark n shit", [], [], [])
asters_room = Room("Aster's room", "shadowy I guess", [], [], [])
bees_room = Room("Bee's room", "happy and ancient", [], [], [])
alexs_room = Room("Alex's room", "well he's dead so the afterlife", [], [], [])
aidans_room = Room("Aidan's room", "this room is made of tears and butchered dreams", [], [], [])
kess_room = Room("Kes's room", "energy shit", [], [], [])
chics_room = Room("Chicago's room", "idk cool bands and shit", [], [], [])
coms_room = Room("Comrade's room", "nurs-y stuff and probably gadgets", [], [], [])
blacks_room = Room("Blackwell's room", "badassery everywhere", [], [], [])

entry.adj = [levis_room, lucys_room, alexs_room, aidans_room]
lucys_room.adj = [entry, levis_room, asters_room, bees_room, coms_room, alexs_room]
levis_room.adj = [entry, lucys_room, asters_room]
asters_room.adj = [lucys_room, levis_room, bees_room]
bees_room.adj = [coms_room, lucys_room, asters_room]
alexs_room .adj = [entry, aidans_room, kess_room, chics_room, coms_room, lucys_room]
aidans_room.adj = [entry, alexs_room, kess_room, blacks_room]
kess_room.adj = [blacks_room, aidans_room, alexs_room, chics_room]
chics_room.adj = [kess_room, alexs_room, coms_room]
coms_room.adj = [chics_room, alexs_room, lucys_room, bees_room]
blacks_room.adj = [aidans_room, kess_room]

house = House([entry, lucys_room, levis_room, asters_room, bees_room, \
               alexs_room, aidans_room, kess_room, chics_room, \
               coms_room, blacks_room])

lucy = Person("Lucy", "She has curly hair and bright green eyes", lucys_room)
levi = Person("Levi", "She has red hair and looks vaguely angry all the time", levis_room)
aster = Person("Aster", "He has black hair, black eyes - black everything, really. Except he's very pale.", asters_room)
bee = Person("Bee", "Blue hair", entry)
alex = Person("Alex", "Blond and rich", entry)
aidan = Person("Aidan", "sad all the time poor baby", entry)
kes = Person("Kes", "orange asshole", kess_room)
chic = Person("Chicago", "blue hair, badass", chics_room)
com = Person("Comrade", "nurse, super nice", coms_room)
black = Person("Blackwell", "fuckin badass all the way", blacks_room)

key = Object("key", "It's a small, brass key.", "a ", entry, True)
bottle = Object("bottle", "It's a clear plastic bottle.", "a ", entry, True)
book = Object("book", "It's a small book, titled 'Jesus Calling'.", "a ", entry, True)
umbrella = Object("umbrella", "It's a purple umbrella.", "an ", entry)

char_list = [lucy, levi, aster, bee, alex, aidan, kes, chic, com, black]
obj_list = [key, bottle, book, umbrella]

for room in house.rooms:
    for obj in obj_list:
        if obj.loc == room:
            room.obj.append(obj)
    for char in char_list:
        if char.loc == room:
            room.pers.append(char)
            
val = True
print("""You stand before a house. Within this house... There are many dark and
painful things that lurk. If you choose to enter, you may never reemerge - and
if you do... you will not be the same.
""")
print("What do you want to do?")
while True:
    print("\n['enter']\n['turn back']\n")
    inp = input()
    print("")
    if inp.lower() == "turn back":
        print("""
A wise decision. You step away from the terrible house,
and flee the very sight of it.\n""")
        val = "turn back"
        break
    elif inp.lower() == "enter":
        mads.loc = entry
        print("""Very well.
As your hand closes on the door knob, a shudder runs down your spine.
Nonetheless, you swing the door open with a creak, and step over the threshold.
The door eases to a shut behind you of its own accord.
""")
        print("You are standing in "+mads.loc.name+".")
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
        if mads.inven != []:
            print("['check inventory']")
        print("['go to ROOM']")
        if mads.loc.pers != []:
            char_str = ""
            for char in mads.loc.pers:
                if char_str == "":
                    char_str += " "+char.name
                else:
                    char_str += ", "+char.name
            print("['examine CHARACTER']"+" ("+char_str+" )")
            print("['talk to CHARACTER']")
        if mads.loc.obj != []:
            obj_str = ""
            for obj in mads.loc.obj:
                if obj_str == "":
                    obj_str += " "+obj.name
                else:
                    obj_str += ", "+obj.name
            print("['examine OBJECT']"+" ("+obj_str+" )")
            for obj in mads.loc.obj:
                if obj.was_examined:
                    if obj.movable:
                        print("['take "+obj.name+"']")
    print("")
    inp = input()
    print("")

    val = "invalid"
        
    # If the command is to check the inventory...
    if inp.lower().startswith("check"):
        val = True
        print(mads.check_inven())
        
        while True:

            if val == True:
                inven_str = ""
                for obj in mads.inven:
                    if inven_str == "":
                        inven_str += " "+obj.name
                    else:
                        inven_str += ", "+obj.name
                print("")
                print("['examine OBJECT']"+" ("+inven_str+" )")
                print("['close backpack']")

            print("")
            inp = input()
            print("")

            val = "invalid"
            
            if inp.lower().startswith("examine"):
                val = True
                target = lol_obj
                for obj in mads.inven:
                    if obj.name == inp[8:].lower().strip("."):
                        target = obj
                        if target not in mads.inven:
                            val = "object not in inven"
                if target == lol_obj:
                    val = "invalid examine target"
                if val == True:
                    print(target.describe())
            if inp == "close backpack":
                val = True
                print("You zip up your backpack.\n")
                break

            if val == "invalid":
                print("[not a valid command]")
            if val == "object not in inven":
                print("[that object is not in your inventory]")
            if val == "invalid examine target":
                print("[not a valid target]")
            

    # If the command is for the player to move...
    if inp.lower().startswith("go to"):
        target_room = lol_place
        val = True
        for room in house.rooms:
            if room.name.lower() == inp[6:].lower().strip("."):
                target_room = room
        if target_room not in mads.loc.adj:
            val = "invalid room"
        if target_room == mads.loc:
            val = "already there"
        if val == True:
            mads.loc = target_room
            print("You are standing in "+mads.loc.name+".")
            print(mads.loc.describe())
            print("")

    # If the command is to examine an object or character...
    if inp.lower().startswith("examine"):
        target = lol_obj
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
        if target == lol_obj:
            val = "invalid target"
        if val == True:
            print(target.describe())
            print("")

    # If the command is to take an object...
    if inp.lower().startswith("take"):
        target_obj = lol_obj
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
        if target_obj == lol_obj:
            val = "invalid target"
        if val == True:
            mads.inven.append(target_obj)
            mads.loc.obj.remove(target_obj)
            print("You take the "+target_obj.name+" and slip it in your backpack.\n")

    # If the command is to talk to a character...
    if inp.lower().startswith("talk to"):
        val = True
        target_pers = lol_obj
        for pers in char_list:
            if pers.name.lower() == inp[8:].lower().strip("."):
                target_pers = pers
                if target_pers not in mads.loc.pers:
                    val = "person not here"
        if target_pers == lol_obj:
            val = "invalid target"
        if val == True:
            print(target_pers.talk())

    # If an invalid command was entered...
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
