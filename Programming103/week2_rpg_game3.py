""" Simple RPG text-based game, based on idea from course's JSON_adventure game,
    whose programme is here as well.
    I didn't bother explaining rules here, or creating try, excepts, etc.

    Basically you have to move, pick up (or not) items and not get eaten by monster in 2x2 matrix.
    Valid moves are horizontal or vertical in the matrix of 'rooms'.
    Each move loses one unit of health.

    You lose if you get eaten by the Monster, or health is otherwise run down to zero.
    You win if you don't lose and you picked up the 3 items of 'loot'.
"""

class Player:
    def __init__(self):
        print("Please enter your name.")
        self.get_name()
        print("Welcome {}.".format(self.name))
        self.health = 5
        self.inventory = []
        self.player_position = [0, 0]

    # allow player to input their name
    def get_name(self):
        self.name = input()

    # create vectors for player moves (North, South East or West are player inputs to this fn.)
    def new_direction(self):
        self.nsew = input()
        if self.nsew == 'North':
            self.delta = [-1,0]
        elif self.nsew == 'South':
            self.delta = [1,0]
        elif self.nsew == 'East':
            self.delta = [0,1]
        else:
            self.delta = [0,-1]

    # player can pick up items in rooms
    def get(self, loot):
         self.inventory.append(loot)

    # checks health != 0, if == 0 then player dies and game ends
    def status(self):
        if self.health == 0:
            print("Your health is {}. You have the following loot: {}.".format(self.health, self.inventory))
        if self.health == 0:
            print("Unfortunately you are Dead. Better luck next time.")
        elif len(self.inventory) == 3:
            print("You have succeeded, well done! End of game.")
        else:
            pass


class GeoRef:
    def __init__(self, player):
        self.possible_locations = [[0, 0], [0, 1], [1, 0], [1, 1]]
        self.player = player
        self.player_position = [0, 0]

        """ allocate rooms to positions in a dictionary. 
            Reason for doing like this is that keys need to be strings.  
            Is simpler than having a dictionary per location that contains everything, 
            or having room as an object (gets complex reading the data from the object).
        """
        self.loot_list = ["Monster", "Lamp", "Key", "Potion"] # <= reason for this is to be able to pop list once gotten
        self.loot_dict = {"Monster": [1, 1], "Lamp": [1, 0], "Key": [0, 1], "Potion": [0,0]}
        self.room_dict = {"Garden": [1, 1], "Dining Room": [1, 0], "Kitchen": [0, 1], "Hall": [0, 0]}

    # helper function to work out next position after a move
    def add_vectors(self, a, b):
        return [a[0]+b[0], a[1]+b[1]]

    # helper function to get key from a dict value
    def get_key(self, val, a_dict):
        for self.key, value in a_dict.items():
            if val == value:
                return self.key
        return "key doesn't exist"

    # function for player to do stuff in a room
    def room_actions(self):
        room_name = self.get_key(self.player_position, self.room_dict)
        room_loot = self.get_key(self.player_position, self.loot_dict)
        # check loot not taken already
        loot_available = room_loot in self.loot_list
        if room_loot == "Monster":
            print("You are in the {}. There is a Monster.  The Monster has eaten you.".
                  format(room_name))
            self.player.health = 0
        elif loot_available and room_loot != "Monster":
            print("You are in the {}. There is a {}.".
                  format(room_name, room_loot, loot_available))
            print("Do you want to pick up the {}?".format(room_loot))
            X = input()
            if X == "Yes":
                self.player.get(room_loot)
                self.loot_list.remove(room_loot)
        else:
            print("You are in the {}. There is nothing available.".
                  format(room_name))


# create a player with position, and a world with the player and the loot
playerOne = Player()
my_world = GeoRef(playerOne)

# start player's actions before they move
my_world.room_actions()
playerOne.status()

# create a while True loop that you can break out of
game_go = True
while game_go:
    # get player to move
    check_function = 0  # <= to control asking for direction
    while check_function == 0:
        print("Which direction?")
        playerOne.new_direction()
        check_position = my_world.add_vectors(my_world.player_position, playerOne.delta)
        if check_position in my_world.possible_locations:
            my_world.player_position = check_position
            check_function = 1
            # use up one health unit due to the move
            playerOne.health -= 1
        else:
            print("illegal Move")

        # actions in a room
        my_world.room_actions()
        playerOne.status()
        if playerOne.health == 0 or len(playerOne.inventory) == 3:
            game_go = False # <= breaks out of the while True loop














