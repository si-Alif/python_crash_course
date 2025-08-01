# 6.1
info1 = {
  "first_name" : "john",
  "last_name": "doe",
  "age": 30,
  "city": "ohio",
}

for key , val in info1.items() :
  if type(val) is not int :
    print(f"My friend's {key} is {val.title()}. \n ")
  else :
    print(f"My friend's {key} is {val}. \n")

# 6.2
favorite_numbers = {
  "Alice" : 7,
  "Bob" : 42,
  "Charlie" : 3,
  "Diana" : 8,
  "Eve" : 1,
}

for name , num in favorite_numbers.items() :
  print(f"{name}'s favorite number is {num}.")

# 6.3 & 6.4
glossary = {
  "list" : "A collection of items in a particular order.",
  "dictionary" : "A collection of key-value pairs.",
  "tuple" : "An immutable collection of items.",
  "set" : "A collection of unique items.",
}

glossary['function'] = "A block of reusable code that performs a specific task."
glossary['loop'] = "A control structure that repeats a block of code."
glossary['variable'] = "A named location in memory to store data."
glossary['iffy'] = "A chain conditional statement that executes code based on a condition."

for term , defn in glossary.items() :
  print(f"\n{term.title()}: \n\t {defn}")


# 6.5
rivers = {
  "padma" : "bangaladesh",
  "padma" : "india",
  "nile" : "egypt",
  "amazon" : "brazil",
  "mississippi" : "usa",
}

for river, country in rivers.items() :
    print(f"The {river.title()} runs through {country.title()}.")

for k in set(rivers.keys()) :
  print(f"River : {k.title()}")

for val in rivers.values() :
  print(f"Country : {val.title()}")


# 6.6
fav_lan = {
    'Alice': 'Python',
    'Bob': 'Java',
    'Charlie': 'JavaScript',
    'Diana': 'C++',
    'Eve': 'Ruby',
}

all_member = ['Alice', 'Bob', 'Charlie', 'Hank', 'Eve', 'Frank' , 'Grace', 'Diana']

friends = ['Alice', 'Bob', 'Charlie','Hank']

for voter in all_member:
    print(f"Hi ! {voter}")
    lan = fav_lan.get(voter)

    if lan is not None and voter in friends :
        print(f"{voter} , I see you like {lan}")
    elif lan is not None and voter not in friends :
        print(f"{voter} , So you like {lan} . Can we friends ?")
    elif lan is None and voter in friends :
        print(f"{voter} , Hey , participate already ...")
    else :
        print(f"{voter} , Can we please get your valuable vote ? ")


# 6.7
info2 = {
  "first_name" : "jane",
  "last_name": "doe",
  "age": 25,
  "city": "ohio",
}

info3 ={
  "first_name" : "joey",
  "last_name": "doe",
  "age": 10,
  "city": "ohio",
}

people = [info1, info2, info3]

for person in people :
  if person['first_name'] == "john" :
    for key , val in person.items() :
      if type(val) is not int :
          print(f"My friend's {key} is {val.title()} ")
      else :
          print(f"My friend's {key} is {val}")
  elif person["first_name"] == "jane":
    for key , val in person.items() :
      if type(val) is not int :
          print(f"My friend's wife jane , her {key} is {val.title()} ")
      else :
          print(f"My friend's wife jane , her {key} is {val}")
  else :
    for key , val in person.items() :
      if type(val) is not int :
          print(f"My friend's daughter joey , her {key} is {val.title()} ")
      else :
          print(f"My friend's daughter joey , her {key} is {val}")


# 6.8
pets = [
  {"cat" : "joby"},
  {"dog" : "boby"},
  {"hamster" : "coby"},
  {"snail" : "doby"},
]

for pet in pets :
    print(f"{list(pet.keys())[0]} is owned by {list(pet.values())[0]}")

# 6.9
fav_places = {
  "john" : ["tokyo" , "switzerland" , "paris"],
  "jane" : ["tokyo" , "new york" , "egypt"],
  "alice" : ["china" , "rome"]
}

for person , places in fav_places.items() :
  print(f"{person}'s favorite places are :")
  for place in places :
    print(f"\t\t\t\t{place}")


# 6.10 --> skipped same as 6.9

# 6.11
cities ={
  "tokyo" : {
    "country" : "japan",
    "population" : 13_000_000,
    "fact" : "Dreamy ... ",
  },
  "paris" : {
    "country" : "france",
    "population" : 2_000_000,
    "fact" : "Famous for the Eiffel Tower",
  },
  "ohio" :{
    "country" : "usa",
    "population" : 10_000_000,
    "fact" : "only in ohio < 3 o((⊙﹏⊙))o."
  }
}

for city , info in cities.items() :
  print(f"{city.title()} :")
  for key , val in info.items() :
    print(f"\t{key.title()} : {val}")

