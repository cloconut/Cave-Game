
# - - - - - - - x - - - - - - - #

from cave import Cave
from character import Character, Enemy, Friend, Merchant
from item import Item, Defence, Offence


asriel = Enemy("ASRIEL DREEMURR", "The absolute GOD of hyperdeath.", 100, 100)
asriel.set_defconvo("I don't need ANYONE!!")
# asriel.describe()
# asriel.get_name()
# asriel.get_health()



# - - - - - - - SPARE CODE - - - - - - - #

# print("What will you fight with?")
# combat_weapon = input()
# asriel.fight(combat_weapon)

# realknife = Item("Real Knife", "Offensive counterpart to the LOCKET")

# realknife.describe()

# bag = ["Mercy", "knife"]

# if Item in bag == None:
#     print("You have no items in your possession.")
# else:
#     print("You possess the following items:")
#     for Item in bag:
#         print(Item)


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

# # (Neutral)
#     def set_convo_intro(self, intro_convo):
#         self.introconvo = intro_convo
# # (Passive)
#     def set_convo_pas(self, pas_convo):
#         self.pasconvo = pas_convo
# # (Agitated)
#     def set_convo_ag(self, ag_convo):
#         self.agconvo = ag_convo