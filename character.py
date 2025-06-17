
# - - - - - - - CHARACTER SUPERCLASS - - - - - - - #

class Character():
    def __init__(self, char_name, char_description, char_health):

        self.name = char_name                      # Name
        self.description = char_description        # Description (on note)
        self.health = char_health                  # Default health
        self.defconvo = None                       # Default conversation

#   NAME

    def get_name(self):
        print(self.name)
    
#   DESCRIPTION

    def describe(self):
        print("The note reads: ")
        print(self.name + ":")
        print(self.description)

#   STATISTICS

    def get_health(self):
        print(self.name + "'s health is at:")
        print(self.health)
    
#   DEFAULT CONVERSATION

    def set_convo(self, convo):
        self.convo = convo

    def get_convo(self):
        print(self.convo)

# - - - - - - - ENEMY SUBCLASS - - - - - - - #

class Enemy(Character):
    def __init__(self, char_name, char_description, char_health, en_attack):
        super().__init__(char_name, char_description, char_health)

        self.exhaust = 0            # Level of exhaustion 
        self.attack = en_attack     # Attack damage dealt (per attack)

# - - - - - - - ENEMY METHODS - - - - - - - #

# - - - - - - - FRIEND SUBCLASS - - - - - - - #

class Friend(Character):
    def __init__(self, char_name, char_description, char_health):
        super().__init__(char_name, char_description, char_health)

# - - - - - - - FRIEND METHODS - - - - - - - #

    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + "]: " + self.conversation)
        else:
            print(self.name + " isn't in the mood to talk.")

# - - - - - - - MERCHANT SUBCLASS - - - - - - - #

class Merchant(Friend):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

# - - - - - - - MERCHANT METHODS - - - - - - - #

# - - - - - - - x - - - - - - - #