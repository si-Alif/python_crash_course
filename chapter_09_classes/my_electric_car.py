import electric_car as EC

my_battery =  EC.Battery(40)

my_electric_car = EC.Electric_Car("Tesla" , "Model S" , 2022 , my_battery.get_battery_size())

print(my_electric_car.get_descriptive_name())
my_electric_car.describe_battery()
my_electric_car.fill_gas_tank()