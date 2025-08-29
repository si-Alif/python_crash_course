"""A Simple attempt to model a car"""

class Car :
    def __init__(self ,brand , model , year ):
        """Initialize attributes to describe a car"""
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = .001

    def update_odometer(self , milage ):
        """A setter method to set odometer value"""
        if milage >= self.odometer_reading :
            self.odometer_reading = milage
        else :
            print("You can't roll back an odometer reading")

    def get_odometer_reading(self) :
        """A getter method to get odometer value"""
        return self.odometer_reading

    def get_descriptive_name(self) :
        return f"{self.brand} {self.model} {self.year}".title()

    def read_odometer(self) :
        """Print the odometer reading"""
        print(f"This car has {self.odometer_reading} miles on it")

    def fill_gas_tank(self) :
        """Simulate filling up the gas tank of the car"""
        print("Filling gas tank")




