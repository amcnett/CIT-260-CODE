# The SUV class represents a sport utility vehicle. It
# is a subclass of the Automobile class.

import automobile

class SUV(automobile.Automobile):
    # The __init__ method caccepts arguments for the
    # SUV's make, model, mileage, price, and passenger
    # capacity.
    
    def __init__(self, make, model, mileage, price, pass_cap):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        super().__init__(make, model, mileage, price) # note NO self
        
        # Initialize the __pass_cap attribute.
        self.__pass_cap = pass_cap

    # The set_pass_cap method is the mutator for the
    # __pass_cap attribute.

    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    # The get_pass_cap method is the accessor for the
    # __pass_cap attribute.

    def get_pass_cap(self):
        return self.__pass_cap
