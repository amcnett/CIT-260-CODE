# introduction to classes and objects

# Create a class called Character​
# Each character should have a name, health, class* (e.g. wizard, zombie, ranger) ​
# Create default and overloaded __init__ functions​
# Create two objects:​
#### One with defaults​
#### One with overloaded (user specified values)

class Character:
    def __init__(self, name=None, health=None, character_class=None):
        if name is not None:
            self.name = name
        else:
            self.name = "bob"
        if health is not None:
            self.health = health
        else:
            self.health = 100
        if character_class is not None:
            self.character_class = character_class
        else:
            self.character_class = "Wizard"


def main():
   
   thebob = Character() # default init
   print(thebob.name)
   print(thebob.health)

   thebob2 = Character("bobby", 50, "Zombie") # overloaded init
   print(thebob2.name)
   print(thebob2.health)

   return
    

if __name__ == '__main__':
    main()