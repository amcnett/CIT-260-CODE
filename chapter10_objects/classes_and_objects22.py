# introduction to classes and objects

# Create a class called Character​
# Each character should have a name, health, class* (e.g. wizard, zombie, ranger) ​
# Create default and overloaded __init__ functions​
# Create two objects:​
#### One with defaults​
#### One with overloaded (user specified values)

class Character:

    # init method -- constructor
    def __init__(self, name=None, health=None, character_class=None):
        if name is not None:
            self.__name = name
        else:
            self.__name = "bob"
        if health is not None:
            self.__health = health
        else:    
            self.__health = 100
        if character_class is not None:
            self.__character_class = character_class
        else:
            self.__character_class = "Zombie"

def main():
   thebob = Character("kevin", 10, "Wizard") # calls init method -- overloaded init
   print(thebob._Character__name)
   print(thebob.__health)
   print(thebob.__character_class)

   thebob2 = Character() # calls init method -- default init
   print(thebob2.__name)
   print(thebob2.__health)
   print(thebob2.__character_class)

   print(thebob)


   return    

if __name__ == '__main__':
    main()