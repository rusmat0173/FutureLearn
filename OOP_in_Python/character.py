class Character():
    # class instance of a set names of all characters
    knowledge = set()

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.active = True

    # Describe this character
    def describe(self):
        print(self.name + ", " + self.description + " is here!" )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

    # fill in the class attribute that lists all characters
    def add_name_to_set(self):
        # This is how we refer to a class variable - classname.varname
        Character.knowledge.add(self.name)

    # be able to interrogate a character for a list of names
    def list_names(self):
        print(Character.knowledge)


# Enemy is a subclass of character
class Enemy(Character):
    # note use of super class constructor, super().__init__, to make clear you are inheriting a class above
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.active = True

    def describe(self):
        if self.active == True:
            print(self.name + ", " + self.description + " is here!")
        else:
            print(self.name + " is fast asleep, keep quiet ...")

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        print(self.weakness)

    def fight(self, combat_item):
        if self.active == True:
            if combat_item == self.weakness:
                self.active = False
                print("You fend " + self.name + " off with the " + combat_item + " and he falls into a long sleep!")
                return True
            else:
                print(self.name + " crushes you, puny adventurer!")
                print("Game over. Better luck next time.")
                return False
        else:
            print(self.name + " doesn't want to fight.")

    def hug(self):
        print(self.name + " crushes you in a hug. You die!")
        print("Game over. Better luck next time.")
        return False

    def bribe(self):
        print(self.name + " cannot be bribed. He eats you!")
        print("Game over. Better luck next time.")
        return False

# Friend is a subclass of character
class Friend(Character):
    # note use of super class constructor, super().__init__, to make clear you are inheriting a class above
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.active = True
        self.will_fight = None
        self.will_hug = None
        self.will_bribe = None
        self.gift = None

    def describe(self):
        if self.active == True:
            print(self.name + ", " + self.description + " is here!")
        else:
            print(self.name + " is fast asleep, keep quiet ...")

    def fight(self, combat_item):
        if self.will_fight == True:
            print(self.name + " crushes you, puny adventurer!")
            print("Game over. Better luck next time.")
            return False
        else:
            print(self.name + " doesn't want to fight.")

    def hug(self):
        if self.will_hug == True:
            print(self.name + " that was a nice hug.")
            print(self.name + " gives you a gift of a " + self.gift + ".\n")
            return True
        else:
            print(self.name + " doesn't like hugs.\n")
            return False

    def bribe(self):
        if self.will_bribe == True:
            print(self.name + " likes bribes.")
            print(self.name + " gives you a gift of a huge " + self.gift + ".\n")
            return True
        else:
            print(self.name + " doesn't take bribes.\n")
            return False