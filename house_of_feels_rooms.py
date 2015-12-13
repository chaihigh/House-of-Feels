from house_of_feels_classes import *

living_room = Room("living room", "The front door is here. On one wall,\n"
                   "there is a couch, and across from it is a TV stand topped with a television.", [], [], [], [], "the ")
lucys_room = Room("Lucy's room", "idk atm", [], [], [], [])
lucys_bath = Room("bathroom", "asdlkf", [], [], [], [], "the ")
lucys_closet = Room("closet", "asdfsldfjfj", [], [], [], [], "the ")
levis_room = Room("Levi's room", "dark n shit", [], [], [], [])
levis_bath = Room("bathroom", "hhsdf", [], [], [], [], "the ")
levis_closet = Room("closet", "laslkdfl", [], [], [], [], "the ")
asters_room = Room("Aster's room", "shadowy I guess", [], [], [], [])
asters_bath = Room("bathroom", "alsdff", [], [], [], [], "the ")
asters_closet = Room("closet", "lsdflsdlf", [], [], [], [], "the ")
bees_room = Room("Bee's room", "happy and ancient", [], [], [], [])
bees_closet = Room("closet", "asdfsdfasdf", [], [], [], [], "the ")
alexs_room = Room("Alex's room", "well he's dead so the afterlife", [], [], [], [])
alexs_bath = Room("bathroom", "asdff", [], [], [], [], "the ")
alexs_closet = Room("closet", "lsl", [], [], [], [], "the ")
aidans_room = Unlit("Aidan's room", "this room is made of tears and butchered dreams", [], [], [], [], "", False, False, True)
aidans_bath = Room("bathroom", "asdfdf", [], [], [], [], "the ")
aidans_closet = Room("closet", "aaasd", [], [], [], [], "the ")
kess_room = Room("Kes's room", "energy shit", [], [], [], [])
kess_closet = Room("closet", "lsdlfdf", [], [], [], [], "the ")
chics_room = Room("Chicago's room", "idk cool bands and shit", [], [], [], [])
chics_bath = Room("bathroom", "uffdd", [], [], [], [], "the ")
chics_closet = Room("closet", "sdff", [], [], [], [], "the ")
coms_room = Room("Comrade's room", "nurs-y stuff and probably gadgets", [], [], [], [])
coms_closet = Room("closet", "sdflsdfo", [], [], [], [], "the ")
blacks_room = Room("Blackwell's room", "There's a desk.", [], [], [], [])
blacks_closet = Room("closet", "lsdll", [], [], [], [], "the ")
basement = Unlit("basement", "very dark, can't see", [], [], [], [], "the ", False)
west_hall = Room("west hallway", "There's a photo on the wall.", [], [], [], [], "the ")
north_hall = Room("north hallway", "the hallway that is north", [], [], [], [], "the ")
landing = Room("second floor landing", "exactly what it sounds like", [], [], [], [], "the ")
sun_room = Room("sun room", "this may not exist later", [], [], [], [], "the ")
sec_hall = Room("hallway", "hallllll", [], [], [], [], "the ")

living_room.adj = [basement, west_hall, north_hall]
lucys_room.adj = [north_hall]
lucys_room.inter = [lucys_bath, lucys_closet]
lucys_bath.adj = [lucys_room, blacks_room]
lucys_closet.adj = [lucys_room]
levis_room.adj = [sec_hall]
levis_room.inter = [levis_bath, levis_closet]
levis_bath.adj = [levis_room, kess_room]
levis_closet.adj = [levis_room]
asters_room.adj = [sec_hall]
asters_room.inter = [asters_bath, asters_closet]
asters_bath.adj = [asters_room]
asters_closet.adj = [asters_room]
bees_room.adj = [north_hall]
bees_room.inter = [alexs_bath, bees_closet]
bees_closet.adj = [bees_room]
alexs_room.adj = [west_hall]
alexs_room.inter = [alexs_bath, alexs_closet]
alexs_bath.adj = [alexs_room, bees_room]
alexs_closet.adj = [alexs_room]
aidans_room.adj = [west_hall]
aidans_room.inter = [aidans_bath, aidans_closet]
aidans_bath.adj = [aidans_room]
aidans_closet.adj = [aidans_room]
kess_room.adj = [sec_hall]
kess_room.inter = [levis_bath, kess_closet]
kess_closet.adj = [kess_room]
chics_room.adj = [sec_hall]
chics_room.inter = [chics_bath, chics_closet]
chics_bath.adj = [chics_room, coms_room]
chics_closet.adj = [chics_room]
coms_room.adj = [sec_hall]
coms_closet.adj = [coms_room]
coms_room.inter = [chics_bath, coms_closet]
blacks_room.adj = [north_hall]
blacks_room.inter = [lucys_bath, blacks_closet]
blacks_closet.adj = [blacks_room]
basement.adj = [living_room]
west_hall.adj = [north_hall, living_room, landing, alexs_room, aidans_room]
north_hall.adj = [west_hall, living_room, bees_room, lucys_room, blacks_room]
landing.adj = [sun_room, sec_hall, west_hall]
sun_room.adj = [landing]
sec_hall.adj = [landing, coms_room, chics_room, levis_room, kess_room, asters_room]

house = House([living_room, lucys_room, lucys_bath, lucys_closet, \
               levis_room, levis_bath, levis_closet, asters_room,
               asters_bath, asters_closet, bees_room, bees_closet, \
               alexs_room, alexs_bath, alexs_closet, aidans_room, \
               aidans_bath, aidans_closet, kess_room, kess_closet, \
               chics_room, chics_bath, chics_closet, coms_room, \
               coms_closet, blacks_room, blacks_closet, basement, \
               west_hall, north_hall, landing, sun_room, sec_hall])
