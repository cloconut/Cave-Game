
# - - - - - - - CHARACTER SUPERCLASS - - - - - - - #

class Character():
    def __init__(self, char_name, char_description, char_health):
        self.name = char_name
        self.description = char_description
        self.health = char_health

# - - - - - - - NOTES - - - - - - - #

#   Common features in Character
# 1. A name
# 2. A note entry including their description
# 3. Health stats

# - - - - - - - METHODS CHARACTER - - - - - - - #

# 1. NAME

    def set_name(self, char_name):
        self.name = char_name

    def get_name(self):
        return self.name
    
# 2. DESCRIPTION

    def describe(self):
        print(self.name + ' is here!')
        print(self.description)

# 3. STATISTICS

    def set_health(self, char_health):
        self.health = char_health

    def get_health(self):
        return self.health

# - - - - - - - ENEMY SUBCLASS - - - - - - - #

class Enemy(Character):
    def __init__(self, char_name, char_description, char_health):
        super().__init__(self, char_name, char_description, char_health)
        self.exhaust = 0

# - - - - - - - NOTES - - - - - - - #

#   Enemy inherits from Character and adds:
# 1. Weakness
# 2. Fight initiation
# 3. Level of exhaustion
# 4. Ability to steal from enemy

# - - - - - - - ENEMY METHODS - - - - - - - #

# 1. WEAKNESS

    def set_weakness(self, weakness):
        self.weakness = weakness

# FIGHT

# EXHAUSTION
    def exhaust(self):
        return

# STEAL
    def steal(self):
        if self.exhaust >= 80:
            print("You stole PLACEHOLDER from " + self.name)
        else:
            print(self.name + "is on high alert")


# - - - - - - - FRIEND SUBCLASS - - - - - - - #

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None

# - - - - - - - NOTES - - - - - - - #

#   Friend inherits from character and adds:
# - Introductory dialogue
# - Varied passive dialogue

# - - - - - - - FRIEND METHODS - - - - - - - #

    def pat(self):
        print(self.name + "pats you")

# - - - - - - - MERCHANT SUBCLASS - - - - - - - #

class Merchant(Friend):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

# - - - - - - - NOTES - - - - - - - #

#   Merchants inherit from Friend and adds:
# - The ability to return currency when item is given

# - - - - - - - MERCHANT METHODS - - - - - - - #

# - - - - - - - x - - - - - - - #




# Idk what this is for

#     def set_combat_item(self, combat_item):
#         self.combat_item = combat_item

#     def fight(self, combat_item):
#         if combat_item == self.weakness:
#             print("[" + self.name + "]: " + "What... is that.")
#             print("You've discovered the enemy's weakness")
#             print("Attacker's defense has dropped by 50%")

#     def fight(self):
#         print(self.name + "isn't bothered enough.")
#         return True
    
#     def set_attack(self, char_attack):
#         self.attack = char_attack

#     def get_attack(self):
#         return self.attack
    
# # 4. DIALOGUE

#     def talk(self):
#         if self.conversation is not None:
#             print("[" + self.name + "]: " + self.conversation)
#         else:
#             print(self.name + "really isn't in the mood.")

# # (Neutral)
#     def set_convo_intro(self, intro_convo):
#         self.introconvo = intro_convo
# # (Passive)
#     def set_convo_pas(self, pas_convo):
#         self.pasconvo = pas_convo
# # (Agitated)
#     def set_convo_ag(self, ag_convo):
#         self.agconvo = ag_convo