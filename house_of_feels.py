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

    attributes: name, (string), description (string)[, list of Objects, list of Persons]"""

    def __init__(self, name, desc, adj=[], inter=[], obj=[], pers=[]):
        """Store the name, description of, list of Rooms adjacent to, list
        of interior Rooms, list of Objects within, and list of Persons
        within the Room.

        Room, string, string, list of Rooms, list of Rooms, list of Objects,
        list of Persons -> None"""

        self.name = name
        self.desc = desc
        self.adj = adj
        self.inter = inter
        self.obj = obj
        self.pers = pers

    def describe_rooms(self):
        """Describe which Rooms are adjacent to this Room.

        Room -> string"""
        
        adj_str = ""
        for room in self.adj:
            if len(self.adj) == 1:
                adj_str = room.name
                verb = " is"
            elif len(self.adj) == 2:
                if room == self.adj[-1]:
                    adj_str += " and "+room.name
                else:
                    adj_str = room.name
                verb = " are"
            else:
                if room == self.adj[-1]:
                    adj_str += "and "+room.name
                else:
                    adj_str += room.name+", "
                verb = " are"
                
        inter_str = ""
        for room in self.inter:
            if len(self.inter) == 1:
                inter_str = room.name
                verb = " is"
            elif len(self.inter) == 2:
                if room == self.inter[-1]:
                    inter_str += " and "+room.name
                else:
                    inter_str = room.name
                verb = " are"
            else:
                if room == self.inter[-1]:
                    inter_str += "and "+room.name
                else:
                    inter_str += room.name+", "
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
        for obj in self.obj:
            if len(self.obj) == 0:
                obj_str = ""
            elif len(self.obj) == 1:
                obj_str = obj.art+obj.name
            elif len(self.obj) == 2:
                if obj == self.obj[-1]:
                    obj_str += " and "+obj.art+obj.name
                else:
                    obj_str = obj.art+obj.name
            else:
                if obj == self.obj[-1]:
                    obj_str += "and "+obj.art+obj.name
                else:
                    obj_str += obj.art+obj.name+", "
        if len(self.obj) > 0 and len(self.pers) == 0:
            return ("There's no one else in here, but you notice some items around"
                    "the room - "+obj_str+".")
        if len(self.obj) > 0 and len(self.pers) > 0:
            return (pers_str+verb+" here.\n"
                    "You notice some items around the room - "+obj_str+".")

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
    location (Room)[, movable (boolean), was_examined (boolean)]"""

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
    location (Room)[, movable (boolean), was_examined (boolean),
    is_on (boolean)]"""

    def __init__(self, name, desc, art, loc, movable=False, was_examined=False, is_on=False):
        """Store the attributes.

        string, string, string, Rooom, [bool, bool, bool] -> None"""

        Object.__init__(self, name, desc, art, loc, movable, was_examined)
        self.is_on = is_on

    def turn_on(self):
        """Turn the Object on.

        On_or_Off -> None"""

        self.is_on = True
