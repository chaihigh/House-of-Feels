from house_of_feels_lucy import *
from house_of_feels_levi import *
from house_of_feels_aster import *
from house_of_feels_aidan import *
from house_of_feels_alex import *
from house_of_feels_kes import *
from house_of_feels_com import *
from house_of_feels_chic import *
from house_of_feels_black import *
from house_of_feels_bee import *

class House:
    """Satan.

    attributes: list of Rooms"""

    def __init__(self, rooms):
        """Store a list of the House's Rooms.

        House, list of Rooms -> None"""

        self.rooms = rooms

class Room:
    """Pain.

    attributes: name, (string), description (string)[, \
    list of adjacent Rooms, list of interior Rooms, \
    list of Objects, list of Persons, article (string) \
    can_describe (boolean)]"""

    def __init__(self, name, desc, adj=[], inter=[], obj=[], pers=[], art="",
                 can_describe=True):
        """Store the attributes.

        Room, string, string[, list of Rooms, list of Rooms, list of Objects,
        list of Persons, string, boolean] -> None"""

        self.name = name
        self.desc = desc
        self.adj = adj
        self.inter = inter
        self.obj = obj
        self.pers = pers
        self.art = art
        self.can_describe = can_describe

    def describe(self):
        """Describe the Room - 'You are standing in...', description,
        Persons and Objects in Room, and adjadcent and interior Rooms."""

        return ("You are standing in "+self.art+self.name+". "
                +self.desc+"\n"
                +self.describe_contents()+"\n"
                +self.describe_rooms())

    def describe_rooms(self):
        """Describe which Rooms are adjacent to this Room.

        Room -> string"""
        
        adj_str = ""
        for room in self.adj:
            if len(self.adj) == 1:
                adj_str = room.art+room.name
                verb = " is"
            elif len(self.adj) == 2:
                if room == self.adj[-1]:
                    adj_str += " and "+room.art+room.name
                else:
                    adj_str = room.art+room.name
                verb = " are"
            else:
                if room == self.adj[-1]:
                    adj_str += "and "+room.art+room.name
                else:
                    adj_str += room.art+room.name+", "
                verb = " are"
                
        inter_str = ""
        for room in self.inter:
            if len(self.inter) == 1:
                inter_str = room.art+room.name
                verb = " is"
            elif len(self.inter) == 2:
                if room == self.inter[-1]:
                    inter_str += " and "+room.art+room.name
                else:
                    inter_str = room.art+room.name
                verb = " are"
            else:
                if room == self.inter[-1]:
                    inter_str += "and "+room.art+room.name
                else:
                    inter_str += room.art+room.name+", "
                verb = " are"
                
        if inter_str == "":
            return ("From here, you can go to "+adj_str+".")
        else:
            return ("From here, you can go to "+adj_str+".\n"
                    "You can also enter "+inter_str+".")

    def describe_contents(self):
        """Describe the Persons and Objects in the Room.

        Room -> string"""
        if len(self.obj) == 0 and len(self.pers) == 0:
            return ("There's nothing of much interest in the room.\n"
                    "There aren't any people here, either.")
        pers_str = ""
        for pers in self.pers:
            if len(self.pers) == 0:
                pers_str = ""
            elif len(self.pers) == 1:
                pers_str = pers.name
                verb = " is"
            elif len(self.pers) == 2:
                if pers == self.pers[-1]:
                    pers_str += " and "+pers.name
                else:
                    pers_str = pers.name
                verb = " are"
            else:
                if pers == self.pers[-1]:
                    pers_str += "and "+pers.name
                else:
                    pers_str += pers.name+", "
                verb = " are"
        if len(self.obj) == 0 and len(self.pers) > 0:
            return ("There's nothing of much interest in the room, but\n"
                    +pers_str+verb+" here.")
        obj_str = ""
        mov_obj = []
        for obj in self.obj:
            if obj.movable == True:
                mov_obj.append(obj)
        for obj in mov_obj:
            if len(mov_obj) == 0:
                obj_str = ""
            elif len(mov_obj) == 1:
                obj_str = obj.art+obj.name
            elif len(mov_obj) == 2:
                if obj == mov_obj[-1]:
                    obj_str += " and "+obj.art+obj.name
                else:
                    obj_str = obj.art+obj.name
            else:
                if obj == mov_obj[-1]:
                    obj_str += "and "+obj.art+obj.name
                else:
                    obj_str += obj.art+obj.name+", "
        if len(mov_obj) > 0 and len(self.pers) == 0:
            return ("There's no one else in here, but you notice some items around the room - \n"
                    +obj_str+".")
        if len(mov_obj) > 0 and len(self.pers) > 0:
            return (pers_str+verb+" here.\n"
                    "You notice some items around the room - "+obj_str+".")

class Unlit(Room):
    """Create an Unlit Room.

    attributes: name, (string), description (string)[, \
    list of adjacent Rooms, list of interior Rooms, \
    list of Objects, list of Persons, article (string) \
    can_describe (boolean), is_lit (boolean), has_light_source (boolean)]"""

    def __init__(self, name, desc, adj=[], inter=[], obj=[], pers=[], art="", can_describe=False, is_lit=False, has_light_source=False):
        """Store the attributes.

        Unlit, string, string, list of Rooms, list of Rooms,
        list of Objects, list of Persons, string, boolean,
        boolean, boolean -> None"""

        Room.__init__(self, name, desc, adj, inter, obj, pers, art, can_describe)
        self.is_lit = is_lit
        self.has_light_source = has_light_source
    
class Person:
    """Create a Person.

    attributes: name (string), description (string)[, location (Room),
    inventory (list of Objects)]"""

    def __init__(self, name, desc, loc="default", inven=[]):
        """Store the name and location of the Person.

        Person, string, string -> None"""

        self.name = name
        self.desc = desc
        self.loc = loc
        self.inven = inven

    def move_to(self, room):
        """Move the Person to the given Room.

        Person, Room -> None"""

        self.loc = room

    def check_inven(self):
        """Return the contents of the Person's inventory.

        Person -> string"""

        inven_str = ""
        for obj in self.inven:
            if len(self.inven) == 1:
                inven_str = obj.art+obj.name
            elif len(self.inven) == 2:
                if obj == self.inven[-1]:
                    inven_str += " and "+obj.art+obj.name
                else:
                    inven_str = obj.art+obj.name
            else:
                if obj == self.inven[-1]:
                    inven_str += "and "+obj.art+obj.name
                else:
                    inven_str += obj.art+obj.name+", "
        return ("You open up your backpack and check its contents. You have "+inven_str+".")

    def describe(self):
        """Describe the Person.

        Person -> string"""

        return self.desc

    def talk(self):
        """Talk to the Person.

        Person -> function... sure... """

        if self.name == "Lucy":
            return talk_to_lucy()
        if self.name == "Levi":
            return talk_to_levi()
        if self.name == "Aster":
            return talk_to_aster()
        if self.name == "Aidan":
            return talk_to_aidan()
        if self.name == "Alex":
            return talk_to_alex()
        if self.name == "Kes":
            return talk_to_kes()
        if self.name == "Chicago":
            return talk_to_chic()
        if self.name == "Comrade":
            return talk_to_com()
        if self.name == "Blackwell":
            return talk_to_black()
        if self.name == "Bee":
            return talk_to_bee()

class Player(Person):
    """Create a Player.

    attributes: name (string), description (string)[,location (Room),
    inventory (list of Objects), sanity (integer)"""

    def __init__(self, name, desc, loc="porch", inven=[], san=100):
        """Store the Player's attributes.

        Player, string, string, Room, list of Objects, integer -> None"""

        Person.__init__(self, name, desc, loc, inven)
        self.san = san

class Object:
    """Create an Object.

    attributes: name (string), description (string), article (string),
    location (Room or Go_Deeper)[, movable (boolean), was_examined (boolean)]"""

    def __init__(self, name, desc, art, loc, movable=False, was_examined=False):
        """Store the name, description, and location of the Object.

        Object, string, string, string, Room[, bool, bool] -> None"""

        self.name = name
        self.desc = desc
        self.art = art
        self.loc = loc
        self.movable = movable
        self.was_examined = was_examined

    def describe(self):
        """Describe the Object.

        Object -> string"""
        
        self.was_examined = True
        return self.desc

class On_or_Off(Object):
    """Create an Object that can be turned on or off.

    attributes: name (string), description (string), article (string),
    location (Room or Go_Deeper)[, movable (boolean), was_examined (boolean),
    is_on (boolean)]"""

    def __init__(self, name, desc, art, loc, movable=False, was_examined=False, is_on=False):
        """Store the attributes.

        On_or_Off, string, string, string, Rooom[, bool, bool, bool] -> None"""

        Object.__init__(self, name, desc, art, loc, movable, was_examined)
        self.is_on = is_on

    def turn_on(self):
        """Turn the Object on.

        On_or_Off -> None"""

        self.is_on = True

class Go_Deeper(Object):
    """Create an Object that, when examined, presents another set of options
    rather than returning to the main option loop.

    attributes: name (string), description (string), article (string),
    traits (list of Objects), location (Room or Go_Deeper)[, movable (boolean),
    was_examined (boolean)]"""

    def __init__(self, name, desc, art, traits, loc, movable=False, was_examined=False):
        """Store the attributes.

        Go_Deeper, string, string, string, traits, Room[, bool, bool] -> None"""

        Object.__init__(self, name, desc, art, loc, movable, was_examined)
        self.traits = traits

    def describe(self):
        """Describe the Go_Deeper, then head to the options loop.

        Go_Deeper -> None"""

        #print(self.desc+"\n")

        return "go_deeper"

    def go_deeper(self):
        """Go into the options loop for this Go_Deeper.

        Go_Deeper -> None"""

        val = True
        
        while True:
            
            if val == True:
                trait_str = ""
                for obj in self.traits:
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
                        if target not in self.traits:
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

        return ("\nYou turn away from the "+self.name+".")
