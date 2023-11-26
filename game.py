def start_game():
    print("Welcome to Space Odyssey!")
    print("You are an astronaut on a mission to explore a newly discovered planet.")
    print("Your spaceship has crash-landed, and you need to find a way to escape.")
    print("You have three key items to collect: the spaceship's repair manual, a fuel injector, and a communication device.")
    
    inventory = []
    current_room = "Crash Site"
    
    while True:
        if current_room == "Crash Site":
            crash_site()
        elif current_room == "Forest":
            forest()
        elif current_room == "Cave":
            cave()
        elif current_room == "Escape Pod":
            escape_pod()
        else:
            print("Invalid room.")

def crash_site():
    print("You are at the crash site of your spaceship.")
    print("You see the wreckage of your ship scattered around you.")
    
    options = ["Search the wreckage", "Go to the forest"]
    choice = input("What do you want to do? ")
    
    if choice == "Search the wreckage":
        if "repair manual" not in inventory:
            print("You find the spaceship's repair manual.")
            inventory.append("repair manual")
        else:
            print("You have already found the repair manual.")
    elif choice == "Go to the forest":
        current_room = "Forest"
    else:
        print("Invalid choice.")

def forest():
    print("You are in a dense forest.")
    print("You see trees towering above you and hear the sounds of animals in the distance.")
    
    options = ["Continue through the forest", "Go back to the crash site"]
    choice = input("What do you want to do? ")
    
    if choice == "Continue through the forest":
        current_room = "Cave"
    elif choice == "Go back to the crash site":
        current_room = "Crash Site"
    else:
        print("Invalid choice.")

def cave():
    print("You are in a dark cave.")
    print("You can barely see your surroundings.")
    
    options = ["Explore the cave", "Go back to the forest"]
    choice = input("What do you want to do? ")
    
    if choice == "Explore the cave":
        if "fuel injector" not in inventory:
            print("You find a fuel injector in a hidden crevice.")
            inventory.append("fuel injector")
        else:
            print("You have already found the fuel injector.")
    elif choice == "Go back to the forest":
        current_room = "Forest"
    else:
        print("Invalid choice.")

def escape_pod():
    print("You reach the escape pod.")
    print("You use the repair manual to fix the pod.")
    print("You use the fuel injector to fill the pod's fuel tank.")
    print("You use the communication device to contact Earth.")
    print("Your escape pod launches, and you successfully return to Earth.")
    print("Congratulations! You have escaped the planet!")

start_game()
