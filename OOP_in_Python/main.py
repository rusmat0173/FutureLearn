""" uses the room.py's class """

from room import Room
from character import Character
from character import Enemy
from character import Friend

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
garden = Room("Garden")

kitchen.set_description("A scarily sterile kitchen")
kitchen.link_room(dining_hall, "south")
kitchen.link_room(garden, "west")

ballroom.set_description(" A huge palace of lights and mirrors")
ballroom.link_room(dining_hall, "east")
ballroom.link_room(garden, "north")

dining_hall.set_description("Dark, cold and full of cobwebs and rat-like sounds")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")

garden.set_description("A tangled semi-jungle of prickly thorns")
garden.link_room(kitchen, "east")
garden.link_room(ballroom, "south")

dave = Enemy("Dave", "a slimy, stinky zombie")
dining_hall.set_character(dave)
dave.set_conversation("Hey Dude - listen to an old zombie!")
dave.set_weakness("cheese")
dave.add_name_to_set()

duncan = Friend("Duncan", "a shifty-looking elf")
duncan.set_conversation("Ugh, can't I have some peace.")
garden.set_character(duncan)
duncan.will_fight = False
duncan.will_hug = False
duncan.will_bribe = True
duncan.gift = "magnifying glass"
duncan.add_name_to_set()

aurora = Friend("Aurora", "a powerful, magical fairy")
aurora.set_conversation("Sparkly, sparkle.")
ballroom.set_character(aurora)
aurora.will_fight = True
aurora.will_hug = True
aurora.will_bribe = False
aurora.gift = "sapphire"
aurora.add_name_to_set()


current_room = kitchen
player_loot = set()
while True:
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        if inhabitant.active == True:
            inhabitant.talk()
    command = input("Your action?> ")
    if "Enemy" in str(type(inhabitant)) and inhabitant.active == True:
        if command != "fight":
            print("Too late, you've been eaten.")
            print("Game over. Better luck next time.")
            break
        else:
            weapon = input("what with? > ")
            combat = inhabitant.fight(weapon)
            if combat == False:
                break  # < of note: stops game
    elif command == "fight":
        weapon = input("what with? > ")
        combat = inhabitant.fight(weapon)
        if combat == False:
            break  # < of note: stops game
    elif command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "hug":
        likes_hugs = inhabitant.hug()
        if likes_hugs == True:
            player_loot.add(inhabitant.gift)
        else:
            print("Please don't hug.\n")
    elif command == "bribe":
        likes_bribes = inhabitant.bribe()
        if likes_bribes == True:
            player_loot.add(inhabitant.gift)
        else:
            print("Bribes are insulting.\n")

    elif command == "list names":
        try:
            current_room.character.list_names()
        except:
            pass

    if len(player_loot) == 2 and dave.active == False:
        print("You have got all the loot and put the baddie to sleep. Well done. Game ends.")
        break



