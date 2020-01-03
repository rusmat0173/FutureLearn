""" Defines the room class for the [xyz] programme """

class Room:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_rooms = {}
        # we put a character in the room
        self.character = None

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        # print(self.name + " linked rooms :" + repr(self.linked_rooms))

    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(self.name  + ": The " + room.name + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character