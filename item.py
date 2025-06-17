# - - - - - - - NOTES - - - - - - - #

#   There will be 5 item subclasses: 
# Defense, offense, spells (defensive and offensive), food
# COMMON ATTRIBUTES
# - Name or label
# - Description
# DEFENSE
# - How much damage it will reflect
# OFFENSE
# - How much damage it deals
# SPELLS DEFENSIVE
# - If it heals player health
# - Long lasting effect
# SPELLS OFFENSIVE
# - How much damage dealt to opponent health
# - Long lasting effect
# FOOD
# - Amount of health regained

# - - - - - - - ITEM SUPERCLASS - - - - - - - #

class Item():
    def __init__(self, item_name, item_desc):
        self.name = item_name.upper()
        self.description = item_desc

# - - - - - - - SPELL SUPERCLASS - - - - - - - #

class Spell():
    def __init__(self, spell_name, spell_desc, spell_effect):
        self.name = spell_name.upper()
        self.description = spell_desc
        self.effect = spell_effect

# - - - - - - - DEFENSE - - - - - - - #

class Defense(Item):
    def __init__(self, item_name, item_desc, deflect_count):
        super().__init__(item_name, item_desc)
        self.deflect = deflect_count

# - - - - - - - OFFENSE - - - - - - - #

class Offense(Item):
    def __init__(self, item_name, item_desc, damage_count):
        super().__init__(item_name, item_desc)
        self.damage = damage_count

# - - - - - - - FOOD - - - - - - - #

class Food(Item):
    def __init__(self, item_name, item_desc, uphealth_count):
        super().__init__(item_name, item_desc)
        self.uphealth = uphealth_count

# - - - - - - - DEFENSIVE SPELLS - - - - - - - #

class DefSpell(Spell):
    def __init__(self, spell_name, spell_desc, spell_effect, deflect_count):
        self.deflect = deflect_count

# - - - - - - - OFFENSIVE SPELLS - - - - - - - #

class OffSpell(Spell):
    def __init__(self, spell_name, spell_desc, spell_effect, damage_count):
        self.damage = damage_count

# - - - - - - - x - - - - - - - #




    def describe(self):
        print("You stumbled across a" + self.name)
        print(self.description)
