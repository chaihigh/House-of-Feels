from house_of_feels_condition import *

def talk_to_alex():

    print(""" - ['1' - "Hey."]""")
    print(""" - ['2' - Leave the conversation.]""")

    inp = input("\n")
    print("")

    if inp == "1":
        if happy_aidan.is_fulfilled == True:
            print("""Alex smiles at you. "Hey."\n""")
        else:
            print("""Alex stares at you.\n""")
    if inp == "2":
        print("You end the conversation.\n")
        
