# The Car class represents a car. It is a subclass
# of the Automobile class.
import automobile

class Car(automobile.Automobile):
    # The __init__ method accepts arguments for the
    # car's make, model, mileage, price, and doors.
    
    def __init__(self, make, model, mileage, price, doors):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        super().__init__(make, model, mileage, price) # note NO self
        
        # Initialize the __doors attribute.
        self.__doors = doors

    # The set_doors method is the mutator for the
    # __doors attribute.

    def set_doors(self, doors):
        self.__doors = doors

    # The get_doors method is the accessor for the
    # __doors attribute.

    def get_doors(self):
        return self.__doors