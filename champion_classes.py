SuperChampion = __import__('base_champion_class').SuperChampion

class Cleric(SuperChampion):
  '''cleric'''
  init_stats =  {"Health": 6, "Attack": 2, "Defense": 3, "Magic": 9, "Speed": 7}
  attack_weapon = 2
  champion_class = 0# mejor __name__

  def __init__(self, name, race, gender):
    super().__init__(name, race, gender, "Cleric")


class Paladin(SuperChampion):

  init_stats = {"Health": 10, "Attack": 4, "Defense": 8, "Magic": 1, "Speed": 4}
  attack_weapon = 1
  defense_equipment = True
  armor = {'Helmet' : [1,1], 'Gauntlets' : [1,1], 'Chest_armor' : [3,2], 'Leg_armor' : [1,1]}
  champion_class = 3
  def __init__(self, name, race, gender):
    super().__init__(name, race, gender, "Paladin")


class Rogue(SuperChampion):

  init_stats = {"Health": 6, "Attack": 7, "Defense": 4, "Magic": 1, "Speed": 9}
  attack_weapon = 4
  champion_class = 5

  def __init__(self, name, race, gender):
    super().__init__(name, race, gender, "Rogue")
