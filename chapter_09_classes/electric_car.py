"""
A simple attempt to model an electric car

"""
from car import Car

class Battery :
    """
    A simple attempt to model a battery for an electric car\n
    Pass the battery size as an argument to the constructor
    """
    def __init__(self , battery) :
        self.battery_size = battery

    def describe_battery(self) :
        """Print statement stating the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_battery_size(self) :
        """Get battery size"""
        return self.battery_size

    def get_range(self):
        """Get the range based on battery size"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 75:
            range = 250
        print(f"This car can go about {range} miles on a full charge")


class Electric_Car(Car) :
    def __init__(self , brand , model , year , battery_size):
        super().__init__(brand=brand , model=model , year=year) # super() gives access to parent classes data members and methods . Thus that's how we call the parent class constructor via super().__init__()
        self.battery_info = Battery(battery=battery_size) # assigning an instance of the battery class to battery_info attribute of the Electric_Car class

    def describe_battery(self) :
        """Print Battery Capacity info of the car"""
        print(f"This car has a {self.battery_info.get_battery_size()}-kWh battery")

    def fill_gas_tank(self): # overridden method --> this has now more priority than the parent method from child classes perspective
        """Simulate filling up the gas tank of the car if possible"""
        print("This car doesn't have a gas tank")

