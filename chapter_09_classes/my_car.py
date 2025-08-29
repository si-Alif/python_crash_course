from car import Car as CreateCar

my_car = CreateCar('audi' , 'a4' , 2019)

print(my_car.get_descriptive_name())

my_car.fill_gas_tank()

my_car.update_odometer(27)

my_car.update_odometer(23)

my_car.read_odometer()