#!/usr/bin/python3
"""
In this module, the super class for every creature in the champions
"""
import json

class SuperChampion:
  """  """
  races = ["Human", "Elf", "Dwarf", "Hobbit", "Orc"]
  genders = ["Male", "Female", "Other"]
  classes = ["Cleric", "Fighter", "Mage", "Paladin", "Ranger", "Rogue"]
  weapons = ["Bow", "Sword", "Staff(Nico)", "Hammer", "Blade" ]


  def __init__(self, name, race, gender, champion_class):
    """ Initialization of the standard creature """
    self.__name = name
    self.race = race
    self.__gender = gender
    self.__level = 0
    self.__exp = {"current": 0, "for_next": 10, "total": 0}
    self.stat_points = 0
    self.__stats = self.init_stats
    self.__attack_weapon = self.attack_weapon
    self.__armor = {'Helmet' : [0, 0], 'Gauntlets' : [0, 0], 'Chest_armor' : [0,0], 'Leg_armor' : [0,0]}
    self.__death = {}

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    if type(value) != str or len(value) < 1:
      raise TypeError("Invalid Name")
    self.__name = value

  @property
  def race(self):
    return self.races[self.__race]

  @race.setter
  def race(self, value):
    if type(value) != str or len(value) < 1 or value not in self.races:
      raise TypeError("Invalid Race")
    self.__race = self.races.index(value)

  @property
  def level(self):
    return self.__level
  
  @level.setter
  def level(self, value):
    if type(value) != int or value < 0 and value > 100:
        raise TypeError("Invalid value")
    self.__level = value
  
  def __str__(self):
    return "[{}] name: {},  race: {}, gender: {}, level: {}, stats: {}, exp: {}, sp: {}".format(type(self).__name__, self.name,  self.race, self.__gender, self.level, self.__stats, self.__exp, self.stat_points)

  
  def to_json_file(self, file_name):
    """ return the __dict__ information of the given object
    """
    with open(file_name, 'w', encoding='utf-8') as output_file:
        #json.dump(self, output_file)
        json.dump(self.__dict__, output_file)

  @classmethod
  def from_json_file(cls, file_name):
    """ return the __dict__ information of the given object
    """
    with open(file_name, 'r', encoding='utf-8') as input_file:
      data = json.load(input_file)
    
    new_object = object(data[classes]["champion_class"])
    for key in data.keys():
      setattr(new_object, key, data[key])
    return new_object

  @property
  def gender(self):
    return self.__genders[self.__gender]
    
  @gender.setter
  def gender(self, value):
    counter = 0
    for i in self.__genders:
      if i == value:
        return counter  
      counter += 1
    raise ValueError("Value gender not found")
  
  def attack(self, attack_damage):
    total_damage = attack_damage * 2
    print("You did a total damage of {}".format(total_damage))

  @property
  def exp(self):
      total = 'Total experience: {}'. format(self.__exp.get('total'))
      current = 'Current experience: {}'. format(self.__exp.get('current'))
      for_next = 'Experience required to reach the next level: {}'.format(self.__exp.get('for_next'))
      return total + current + for_next

  @exp.setter
  def exp(self, value):
    if type(value) != int or value < 0:
      raise TypeError("Invalid Value")
    self.__exp.update=value
    #self.__exp.update('current') += value
    #self.__exp.update('total') += value
    #self.__exp.update('for next') = 10 - self.__exp.get('current')

  def level_up(self):
  '''level'''
    pass
  
