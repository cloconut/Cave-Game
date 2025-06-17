from cave import Cave
from character import Enemy

def info():

    # - - - - - - - CAVE INFORMATION - - - - - - - #

    # Hollow
    hollow = Cave('Harrowing Hollow')
    hollow.set_note('Its so empty in here...')
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