from house_of_feels_obj import *

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

    return ("\nYou turn away from the "+go_deeper.name+".")
