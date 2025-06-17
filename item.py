
# - - - - - - - ITEM SUPERCLASS - - - - - - - #

class Item():
    def __init__(self, item_name, item_desc):
        self.name = item_name
        self.description = item_desc

# - - - - - - - NOTES - - - - - - - #

# - Name or label
# - Description

# - - - - - - - x - - - - - - - #

# - - - - - - - DEFENCE - - - - - - - #

class Defence(Item):
    def __init__(self, item_name, item_desc, deflect_count):
        super().__init__(item_name, item_desc)
        self.deflect = deflect_count

# - - - - - - - NOTES - - - - - - - #

# - How much damage it will reflect

# - - - - - - - DEFENCE METHODS - - - - - - - #

# - - - - - - - OFFENCE - - - - - - - #

class Offence(Item):
    def __init__(self, item_name, item_desc, damage_count):
        super().__init__(item_name, item_desc)
        self.damage = damage_count

# - - - - - - - NOTES - - - - - - - #

# - How much damage it deals

# - - - - - - - x - - - - - - - #

# - - - - - - - FOOD - - - - - - - #

class Food(Item):
    def __init__(self, item_name, item_desc, uphealth_count):
        super().__init__(item_name, item_desc)
        self.uphealth = uphealth_count

# - - - - - - - NOTES - - - - - - - #

# - Amount of health regained

# - - - - - - - METHODS - - - - - - - #




    def describe(self):
        print("You stumbled across a" + self.name)
        print(self.description)


# er43fgtr - (Carmen)