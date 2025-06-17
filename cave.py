# - - - - - - - NOTES - - - - - - - #

#   Caves will have the following features:
# - An enterance sign displaying its name
# - Caves linked to it / map features
# - Notes from the previous explorer that player finds on entry
# - One enemy minimum
# - One friend minimum (includess merchants)
# - 2 items minimum (defense and attack)

# - - - - - - - CAVE SUPERCLASS - - - - - - - #

class Cave:
    def __init__(self, cave_name):
        self.name = cave_name
        self.note = None
        self.linked_caves = {}
        self.character = None
        self.item = None

# - - - - - - - METHODS (CAVE) - - - - - - - #

# 1. NAME

    def set_name(self, cave_name):
        self.name = cave_name

    def get_name(self):
        return self.name

# 2. LINKED CAVES / MAP FEATURES

    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link

    def get_map(self):
        for direction in self.linked_caves:
            cave = self.linked_caves[direction]
            print('The ' + cave.get_name() + ' is ' + direction)

    def move(self, direction):
        if direction in self.linked_caves[direction]:
            return self.linked_caves[direction]
        else:
            print("You can't go that way")
            return self

# 3. EXPLORER NOTES

    def set_note(self, cave_note):
        self.note = cave_note

    def get_note(self):
        return self.note

    def note(self):
        print(self.note)

# 4. CHARACTERS

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

# 5. ITEMS

    def set_item(self, new_item):
        self.item = new_item

    def get_item(self):
        return self.item

# - - - - - - - x - - - - - - - #