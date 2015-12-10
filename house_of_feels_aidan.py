from house_of_feels_condition import *

def talk_to_aidan():

    print(" - ['1' - Ask about Alex.]")
    print(" - ['2' - Leave the conversation.]")

    inp = input("\n")
    print("")

    if inp == "1":
        happy_aidan.is_fulfilled = True
        print("""Aidan smiles dumbly.\n""")
    if inp == "2":
        print("""You end the conversation.\n""")
