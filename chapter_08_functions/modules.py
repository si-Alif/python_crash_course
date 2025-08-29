def build_prof(first_name , last_name, **kwargs):
	# here the kwargs is a dictionary
	kwargs["first"] = first_name
	kwargs["last"] = last_name
	return kwargs

def describe_pet(pet_name , animal_type = 'cat' ):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")
