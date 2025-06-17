
# - - - - - - - x - - - - - - - #

from cave import Cave
from character import Character, Enemy, Friend, Merchant
from item import Item, Defense, Offense, Spell, DefSpell, OffSpell

# - - - - - - - TEST OBJECTS - - - - - - - #

# CAVE

# ENEMY

def enemytest():
    asriel = Enemy("Asriel Dreemurr", "The absolute GOD of hyperdeath.", 100,)
    asriel.set_weakness("Mercy")



enemytest()




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