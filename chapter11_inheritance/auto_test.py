# This program creates a Car object, a Truck object,
# and an SUV object.

import car, truck, suv

def main():
    # Create a Car object for a used 2001 BMW
    # with 70,000 miles, priced at $15,000, with
    # 4 doors.
    acar = car.Car('BMW', 2001, 70000, 15000.0, 4)

    # Create a Truck object for a used 2002
    # Toyota pickup with 40,000 miles, priced
    # at $12,000, with 4-wheel drive.
    atruck = truck.Truck('Toyota', 2002, 40000, 12000.0, '4WD')

    # Create an SUV object for a used 2000
    # Volvo with 30,000 miles, priced
    # at $18,500, with 5 passenger capacity.
    asuv = suv.SUV('Volvo', 2000, 30000, 18500.0, 5)

    print('USED CAR INVENTORY')
    print('===================')
    
    # Display the car's data.
    print('The following car is in inventory:')
    print('Make:', acar.get_make())
    print('Model:', acar.get_model())
    print('Mileage:', acar.get_mileage())
    print('Price:', acar.get_price())
    print('Number of doors:', acar.get_doors())
    print()
    
    # Display the truck's data.
    print('The following pickup truck is in inventory.')
    print('Make:', atruck.get_make())
    print('Model:', atruck.get_model())
    print('Mileage:', atruck.get_mileage())
    print('Price:', atruck.get_price())
    print('Drive type:', atruck.get_drive_type())
    print()
    
    # Display the SUV's data.
    print('The following SUV is in inventory.')
    print('Make:', asuv.get_make())
    print('Model:', asuv.get_model())
    print('Mileage:', asuv.get_mileage())
    print('Price:', asuv.get_price())
    print('Passenger Capacity:', asuv.get_pass_cap())

# Call the main function.
if __name__ == '__main__':
      main()