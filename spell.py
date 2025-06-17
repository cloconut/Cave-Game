
# # - - - - - - - SPELL SUPERCLASS - - - - - - - #

# class Spell():
#     def __init__(self, spell_name, spell_desc, spell_effect):
#         self.name = spell_name.upper()
#         self.description = spell_desc
#         self.effect = spell_effect

# # - - - - - - - DEFENSIVE SPELLS - - - - - - - #

# # SPELLS DEFENSIVE
# # - If it heals player health
# # - Long lasting effect

# class DefSpell(Spell):
#     def __init__(self, spell_name, spell_desc, spell_effect, deflect_count):
#         self.deflect = deflect_count

# # - - - - - - - OFFENSIVE SPELLS - - - - - - - #

# # SPELLS OFFENSIVE
# # - How much damage dealt to opponent health
# # - Long lasting effect

# class OffSpell(Spell):
#     def __init__(self, spell_name, spell_desc, spell_effect, damage_count):
#         self.damage = damage_count

# # - - - - - - - x - - - - - - - #