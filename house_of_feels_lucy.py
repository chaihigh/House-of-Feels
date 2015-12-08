def talk_to_lucy():

    print("""Lucy gives you a polite smile. "Hey."\n""")

    print("""['1' - "Hey."]""")
    print("""['2' - "Fuck you, Lucy.]""")

    inp = input("\n")
    
    if inp == "1":
        print("""\nLucy asks, "How are you?" """)

        print("")
        print("""['1' - Ask about Aster.]""")
        print("""['2' - Ask about Levi.]""")
        print("""['3' - Leave the conversation.]""")
        
        inp2 = input("\n")

        if inp2 == "1":
            print("""\nHer eyes brighten for a moment \
before she can hide it. "What about him?" """)

        if inp2 == "2":
            print("""\nA flash of something, maybe worry, maybe regret, \
flits over her face. "Yeah, what about her?" """)

        if inp2 == "3":
            print("\nYou end the conversation.")
            
    if inp == "2":
        print("""\nLucy snorts, seemingly more amused than offended. \
"Well, fuck you too, then." She turns away.""")

    return ""
