# - - - - - - - IMPORTING CLASSES - - - - - - - #

# Cave
from cave import Cave
# Character
from character import Character
from character import Enemy, Friend
# Item
from item import Item

# - - - - - - - CAVE INFORMATION - - - - - - - #

# Hollow
hollow = Cave('Harrowing Hollow')
hollow.note = "Its so empty in here..."
# Cavern
cavern = Cave('Crusty Cavern')
cavern.set_note('A strangely crusty cave. The walls are... shedding?')
# Grotto
grotto = Cave('Grotty Grotto')
grotto.set_note('Filthy, grimey, grotty. Untouched since 1812.')
# Dungeon
dungeon = Cave('Dusty Dungeon')
dungeon.set_note('Theres a rustling behind the dust... maybe a splashing?')
# Lake
lake = Cave('Lukewarm Lake')
lake.set_note('A calm and tranquil lake, why dont I go for a dip?')
# Mines
mines = Cave('Merchants Mines')
mines.set_note('How neat. A one stop shop for all necessities.')
# Keep
keep = Cave('The Krakens Keep')
keep.set_note('Theres something in the water.')
# Fissure
fissure = Cave('Freaky Fissure')
fissure.set_note('Its said to be haunted in here, bah?')
# Tunnel
tunnel = Cave('Tyrannical Tunnel')
tunnel.set_note('Its so cold...')
# Rave
rave = Cave('The Cave Rave')
rave.set_note('Oh party party yah')

# - - - - - - - CAVE LINKS - - - - - - - #

# Hollow
hollow.link_cave(cavern, 'south')
# Cavern
cavern.link_cave(hollow, 'north')
cavern.link_cave(grotto, 'east')
cavern.link_cave(mines, 'south')
cavern.link_cave(dungeon, 'west')
# Grotto
grotto.link_cave(lake, 'south')
grotto.link_cave(cavern, 'east')
# Dungeon
dungeon.link_cave(cavern, 'east')
dungeon.link_cave(keep, 'south')
# Lake
lake.link_cave(grotto, 'north')
# Mines
mines.link_cave(cavern, 'north')
mines.link_cave(fissure, 'east')
mines.link_cave(tunnel, 'south')
# Keep
keep.link_cave(dungeon, 'north')
keep.link_cave(rave, 'south')
# Fissure
fissure.link_cave(mines, 'west')
# Tunnel
tunnel.link_cave(mines, 'north')
# Rave
rave.link_cave(keep, 'north')

# - - - - - - - ENEMIES - - - - - - - #

# Gribsy
gribsy = Enemy("Gribsy", "Keeper of the Caves. His IQ is beyond your comprehension.", 1, 1)
gribsy.set_convo("You're wasting my time AND yours, my dear ignoramus.")
hollow.set_character(gribsy)

# Marmite and Kibbie (Crusty Cavern)
marmite = Enemy("Marmite", "Curious dust kitty.", 1, 1)
marmite.set_convo("Marm.")
cavern.set_character(marmite)

kibbie = Enemy("Kibbie", "Skittish dust kitty", 1, 1)
kibbie.set_convo("Kibs")
cavern.set_character(kibbie)

# Humonculus (Dusty Dungeon)
humonculus = Enemy("Humonculus", "A giant beastie made of stone", 1, 1)
humonculus.set_convo("Do you WANT your windshield bricked?")
dungeon.set_character(humonculus)

# Gangalang (Tyrannical Tunnel)
gangalang = Enemy("Gangalang", "Cause 3 enemies is the charm", 1, 1)
gangalang.set_convo("Stop right there! Right there? RIGHT THERE!!")
tunnel.set_character(gangalang)

# Boteko (Freaky Fissure)
boteko = Enemy("Boteko", "This guy is kind of Jank.", 1, 1)
boteko.set_convo("Heart deedee, with a baby")
fissure.set_character(boteko)

# Krakeluss - (Kraken's Keep)
krakeluss = Enemy("Krakeluss", "Hasn't seen the light of day in eons. Don't look into his eyes", 1, 1)
krakeluss.set_convo("This is the end, traveller.")
keep.set_character(krakeluss)

# - - - - - - - FRIENDS - - - - - - - #

# jemmie = Friend("Jemmie", "Temmie cousin")
# jemmie.set_convo("Need any help?")
# cavern.set_character(jemmie)

# - - - - - - - x - - - - - - - #

# blankitem = Item("Test Item", "For test purposes")
# hollow.set_item(blankitem)

# - - - - - - - x - - - - - - - #



bag = []
current_cave = hollow
dead = False

while dead == False:
    print("\n")
    print("As you regain conciousness, you realise you have fallen into an unknown cave.")
    print("\n")
    print("There is a torn journal on the ground, will you take it?")
    print(" > Yes")
    print(" > No")
    print("\n")
    command = input('> ')
    if command == 'yes':
        print("You read the first entry...")
        print("\n")
        print("'"+ current_cave.note + "'")
        print("\n")
    elif command == 'no':
        print("\n")
        print('Not a wise choice, but ok.')
        print("\n")


    character = current_cave.get_character()

    items = current_cave.get_item()



# - - - - - - - COMMANDS - - - - - - - #

    action = input('> ')

    if action == "talk":
        if character is not None:
            character.get_convo()

# - x - #

if dead == True:
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("You have perished.")
    print("\n")
    print("\n")
    print("\n")
    print("\n")

#     elif command == "fight":
#         if isinstance(inhabitant, Enemy):
#             print("Choose your weaponry ")
#             weapon = input()

#             if weapon in bag:
#                 print("You summon the weapon from your bag.")
#             else:
#                 print("You don't have a " + weapon)
                
#             if inhabitant.fight(weapon) == True:
#                 print("You have defeated the enemy.")
#                 current_room.set_character(None)
#             else:
#                 print("You have been defeated by the enemy")
#                 print("Your journey has come to an end")
#                 dead = True
#         else:
#             print("There is no enemy here to defeat")

#     elif command == "pat":
#         if inhabitant is not None:
#             if isinstance(inhabitant, Enemy):
#                 print("You couldn't get close enough to pat" + inhabitant.name())
#             else:
#                 inhabitant.pat()
#         else:
#             print("You tenderly caress absolutely nothing.")

#     elif command == "take":
#         if thing is not None:
#             print("You put the " + thing.name() + "in your bag")
#             bag.append(item.name())
#             current_room.set_item(None)
#         else:
#             print("There's nothing to take.")'
            
#     elif command == "bag":
#         bag = []
#         if Item in bag == None:
#          print("You have no items in your possession.")
#         else:
#             print("You possess the following items:")
#             for Item in bag:
#                 print(Item)

#     current_cave = current_cave.move(command)

# # - - - - - - - x - - - - - - - #