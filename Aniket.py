print("Hello world!")
confess = False
while not confess:
    user_input = input("Admit Aniket is a Good Boy ('y' for YES anything otherwise) : ")
    if user_input == "y" :
        confess = True
        print("\tTHANK YOU!")
    else:
        for _ in range (10):
            print("B-O-O-M!")