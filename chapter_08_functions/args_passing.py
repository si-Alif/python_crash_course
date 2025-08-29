from modules import build_prof as build_profile , describe_pet as des_pet



# def <func_name>(param1 , param2):
    # code

# <func_name>(<arg1> , <arg2>)
# <func_name>(<param1> = <arg1> , <param2> = <arg2>)


# def describe_pet(animal_type = 'cat' , pet_name):
# --> ❌error as the non-default parameters have higher priority so they should be written before the default parameters





des_pet("dog" , "bob")
des_pet(animal_type = "dog" , pet_name = "sophie")
des_pet("bozo")

def get_formatted_name(first_name , last_name , middle_name = ''):
    if middle_name :
        return f"{first_name} {middle_name} {last_name}".title()
    else :
        return f"{first_name} {last_name}".title()


print(get_formatted_name("hero" , "alom"))

def get_json(first_name , last_name , middle_name = "" , age = None):
    info  = {
        "first" : first_name,
        "last" : last_name,
    }
    if middle_name :
        info["middle"] = middle_name
    if age:
        info["age"] = age
    return info

info = get_json("hero" , "alom" , "vanga" , 69)

for key , value in info.items():
    print(f"{key} : {value}")



user_prof = build_profile("hero" , 'alom' , location = 'bogura' , field = 'cs')

for key , val in user_prof.items():
    print(f"{key} : {val}")


