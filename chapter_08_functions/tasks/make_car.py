def make_car(manufacturer , model , **car_info):
    """Build a car info JSON based on info provided by the user"""
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info

