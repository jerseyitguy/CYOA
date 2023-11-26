import random

# Define the list of essential items
essential_items = ["Oxygen Tank", "Spacesuit Helmet", "Repair Kit"]

# Function to check if all essential items are collected
def check_inventory(inventory):
    if len(inventory) == len(essential_items):
        print("Congratulations! You've gathered all the essential items and can now escape the spacecraft.")
        return True
    else:
        return False

# Function to simulate a random encounter
def random_encounter():
    encounter_events = ["You encountered a floating asteroid and narrowly avoided collision.",
                        "You spotted a distress signal from another spacecraft, but it's too far to reach.",
                        "You discovered a hidden compartment containing valuable supplies."]
    random_event = encounter_events[random.randrange(0, len(encounter_events))]
    print(random_event)

# Main game loop
inventory = []
while not check_inventory(inventory):
    # Display the current inventory
    print("Inventory:", inventory)

    # Present a choice of actions
    print("\nWhat do you want to do?")
    print("1. Search for essential items")
    print("2. Explore the spacecraft")

    # Get player input
    action = input("Enter your choice: ")

    if action == "1":
        # Simulate searching for items
        found_item = essential_items[random.randrange(0, len(essential_items))]
        if found_item not in inventory:
            inventory.append(found_item)
            print("You found a", found_item)
        else:
            print("You already have that item.")
    elif action == "2":
        # Trigger a random encounter
        random_encounter()
    else:
        print("Invalid action. Please choose from the available options.")
