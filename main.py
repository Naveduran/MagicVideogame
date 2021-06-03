#!/usr/bin/python3
'''main'''
from champions_classes import Cleric, Paladin, Rogue


mycleric = Cleric("Angui", "Hobbit", "Female")
print(mycleric)
print()

myPaladdin = Paladin("Jerson", "Elf", "Male")
print(myPaladdin)
print()

myRogue = Rogue("Oscar", "Orc", "Male")
print(myRogue)

myRogue.to_json_file("h.txt")
