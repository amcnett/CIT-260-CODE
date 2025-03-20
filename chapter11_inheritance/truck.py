# The Truck class represents a pickup truck. It is a
# subclass of the Automobile class.

import automobile

class Truck(automobile.Automobile):
    # The __init__ method accepts arguments for the
    # truck's make, model, mileage, price, and drive type.
    
    def __init__(self, make, model, mileage, price, drive_type):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        super().__init__(make, model, mileage, price) # note NO self
        
        # Initialize the __drive_type attribute.
        self.__drive_type = drive_type

    # The set_drive_type method is the mutator for the
    # __drive_type attribute.

    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    # The get_drive_type method is the accessor for the
    # __drive_type attribute.

    def get_drive_type(self):
        return self.__drive_type