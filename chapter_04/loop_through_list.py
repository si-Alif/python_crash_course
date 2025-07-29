characters_set_1 = ["wizard" , "panda" , "lizard" , "chameleon"]
characters = ["wizard" , "panda" , "lizard" , "chameleon" , "bear"]

for chars in characters_set_1 :
  print(chars)

print(f"Printing currnt value associated with temp variable chars : {chars}")


for chars in characters :
  print(f"Hey {chars} , what's going on ?")
  print(f"Let's hangout sometimes ? What do you think {chars} ?")

print("Asked each character")


print(chars)

pizzas = ["Pepperoni Pizza" , "BBQ Chicken Pizza" , "Greek Pizza" , "Greek Pizza"]

for pizza in pizzas :
  print(f"I like {pizza}")

print("I really like italian cuisine specially pizza")

pets = ["cat" , 'dog' , 'hamster']

for pet in pets:
  print(f"{pet.title()} would make a great pet")

print("Any of the pet mentioned above would make a great pet")

for nums in range(1 , 3): #first
  print(pizzas[nums])


nums_list = list(range(1,11 ,3))
print(nums_list)

print(sum(nums_list))
print(max(nums_list))
print(min(nums_list))

from_1_to_20 = [value for value in  range(1, 21)]

from_1_to_million = [value for value in range(1 , 1000001)]

# for num in from_1_to_million :
#   print(num)

print(min(from_1_to_million))
print(max(from_1_to_million))
print(sum(from_1_to_million))

odd_in_1_to_20 = [value for value in range(1,21,2)]
print(odd_in_1_to_20)

multiple_of_3_in_3_to_30 = [value for value in range(3 , 31 , 3)]
print(multiple_of_3_in_3_to_30)

cubes_of_nums_in_1_to_10 = [num for num in range(1 ,11)]
print(cubes_of_nums_in_1_to_10)

#slicing a list :
players = ["ronaldo" , 'messi' , "zlatan" , "benzema" , "ozil"]
top_3_favorite = players[:3] #read : First 3 elements are assigned as an output

print(top_3_favorite)

for player in players[:4] :
  print(player.title())


fav_dishes = ["pasta" , "nehari" , "biryani" , "ramen" , "kabuli pulao" , "steak"]

most_fav = fav_dishes[:-3] # 0th till -3rd index

print(most_fav)

# copying a list
my_friends_dishes = fav_dishes[:] # this creates a new list object using fav_dishes list value . Ultimately , my_frineds_dishes and fav_dishes refers to  2 different objects of the same list value

my_friends_dishes.append("kacci")
print(fav_dishes)
print(my_friends_dishes)

print(f"First three items in the list are : {fav_dishes[:3]}")
print(f"Middle three items in the list are : {fav_dishes[1:4]}")
print(f"Last three items in the list are : {fav_dishes[-3:]}")


my_freinds_pizzas = pizzas[:]

pizzas.append("Italian Pizza")
my_freinds_pizzas.append("New York Style Pizza")

print("My favorite pizzas are :")
for pizza in pizzas :
  print(pizza)

print('\n')

print("My friends favorite pizzas are :")
for pizza in my_freinds_pizzas:
  print(pizza)

print('\n')

foods  = []
foods.append(pizzas)
foods.append(fav_dishes)

for food in foods :
  for dish in food :
    print(dish)