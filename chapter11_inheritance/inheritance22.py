# The Automobile class holds general data
# about an automobile in inventory.

class Automobile:
    # The __init__ method accepts arguments for the
    # make, model, mileage, and price. It initializes
    # the data attributes with these values.
    
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        self.test = "bob"  # test is public attributer

    # The following methods are mutators for the
    # class's data attributes.
    
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    # The following methods are the accessors
    # for the class's data attributes.
    
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price
    
    def __str__(self):
        return f"Make: {self.__make}, Model: {self.__model}, Mileage: {self.__mileage}, Price {self.__price}"

# The Car class represents a car. It is a subclass
# of the Automobile class.

class Car(Automobile):
    # The __init__ method accepts arguments for the
    # car's make, model, mileage, price, and doors.
    
    def __init__(self, make, model, mileage, price, doors):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)
        
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
    
    def __str__(self):  # this overrides the parent method for __str__
        return super().__str__() + f", Doors: {self.__doors}"
    


# The Truck class represents a pickup truck. It is a
# subclass of the Automobile class.

class Truck(Automobile):
    # The __init__ method accepts arguments for the
    # truck's make, model, mileage, price, and drive type.
    
    def __init__(self, make, model, mileage, price, drive_type):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)
        
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
    
    def __str__(self):  # this overrides the parent method for __str__
        return super().__str__() + f", Drive Type: {self.__drive_type}"

# The SUV class represents a sport utility vehicle. It
# is a subclass of the Automobile class.

class SUV(Automobile):
    # The __init__ method caccepts arguments for the
    # SUV's make, model, mileage, price, and passenger
    # capacity.
    
    def __init__(self, make, model, mileage, price, pass_cap):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)
        
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
    
    def __str__(self):  # this overrides the parent method for __str__
        return super().__str__() + f", Passenger Capacity: {self.__pass_cap}"

class Evehicle(Automobile):
    def __init__(self, make, model, mileage, price, battery_capacity):
        # self.__make = make  #cannot due because make is private to Automobile
        # self.set_make(make)  # can do but too lazy to do
        # Automobile.__init__(self, make, model, mileage, price)
        super().__init__(make, model, mileage, price)
        self.__battery_capacity = battery_capacity
        # self.__make = "MY AWESOME VEHICLE COMPANY" does not work due to private access
        self.test = "bobby"

    # getter
    def get_battery_capacity(self):
        return self.__battery_capacity
    
    # setter
    def set_battery_capcity(self, batt_cap):
        self.__battery_capacity = batt_cap

    def __str__(self):  # this overrides the parent method for __str__
        return super().__str__() + f", Battery Capacity: {self.__battery_capacity}"

def main():
    # Create a Car object for a used 2001 BMW
    # with 70,000 miles, priced at $15,000, with
    # 4 doors.
    car = Car('BMW', 2001, 70000, 15000.0, 4)
    print(car)

    # Create a Truck object for a used 2002
    # Toyota pickup with 40,000 miles, priced
    # at $12,000, with 4-wheel drive.
    truck = Truck('Toyota', 2002, 40000, 12000.0, '4WD')
    print(truck)

    # Create an SUV object for a used 2000
    # Volvo with 30,000 miles, priced
    # at $18,500, with 5 passenger capacity.
    suv = SUV('Volvo', 2000, 30000, 18500.0, 5)
    print(suv)

    eveh = Evehicle("Honda", "Prologue", 1000, 45000, "90kWh")
    print(eveh)

    # print('USED CAR INVENTORY')
    # print('===================')
    
    # # Display the car's data.
    # print('The following car is in inventory:')
    # print('Make:', car.get_make())
    # print('Model:', car.get_model())
    # print('Mileage:', car.get_mileage())
    # print('Price:', car.get_price())
    # print('Number of doors:', car.get_doors())
    # print()
    
    # # Display the truck's data.
    # print('The following pickup truck is in inventory.')
    # print('Make:', truck.get_make())
    # print('Model:', truck.get_model())
    # print('Mileage:', truck.get_mileage())
    # print('Price:', truck.get_price())
    # print('Drive type:', truck.get_drive_type())
    # print()
    
    # # Display the SUV's data.
    # print('The following SUV is in inventory.')
    # print('Make:', suv.get_make())
    # print('Model:', suv.get_model())
    # print('Mileage:', suv.get_mileage())
    # print('Price:', suv.get_price())
    # print('Passenger Capacity:', suv.get_pass_cap())

    # # Display the e-vehicle data.
    # print('The following e-vehicle is in inventory.')
    # print('Make:', eveh.get_make())
    # print('Model:', eveh.get_model())
    # print('Mileage:', eveh.get_mileage())
    # print('Price:', eveh.get_price())
    # print('Battery Capacity:', eveh.get_battery_capacity())

# Call the main function.
if __name__ == '__main__':
      main()