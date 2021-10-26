#!/usr/bin/env python3

dogs = ["fido", "spot", "lucky"]

cats = ["fluffy", "snowball", "garfield"]

pets = [];

pets.extend(dogs)
pets.extend(cats)

print(pets)
print(dogs)

my_pets = {}
for key in dogs:
   for value in cats:
      my_pets[key] = value
      cats.remove(value)
      break
print("Dictionary from lists :\n ",my_pets)

print("I only own " +  pets[1] +" and " + pets[4]) 

# "I want to adopt fido and garfield too"

#print("I want to adopt " + my_pets[0] + " and " )

print("I want to adopt ",my_pets.get, " and ")
