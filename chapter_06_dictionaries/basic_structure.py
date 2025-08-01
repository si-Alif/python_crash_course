# value structure : {<key> : <value>} --> yep , it's a collection of key-value pairs
# this exact thing is called a hashmap or object in other languages

anime_0 = {
    'title': "Attack on Titan",
    'viewers_aura': 999,
    "details":{
        'genre': "Action",
        'rating': 9.5
        }, # it's a good practice to add the comma at the end of the last key-value pair in a dictionary
}

# accessing values , hashmap name --> [] --> <dictionary_name>[<key>][<further_key_if_available_and_want_to_access]>]
print(f"{anime_0['title']} viewers aura : {anime_0['viewers_aura']}")
print(f"{anime_0['title']}'s rating : {anime_0['details']['rating']}")

# adding new key-value pairs
anime_0['status'] = "Finished"
anime_0['details']["episodes"] = 94

print(f"{anime_0['title']} has {anime_0['details']['episodes']} episodes and is {anime_0['status']}")

# Changing values or a key
anime_0['title'] = "A.O.T"
print(f"{anime_0['title']} has {anime_0['details']['episodes']} episodes and is {anime_0['status']}")

anime_0['also_loves'] = [ "Dragon Ball Z" , "One Piece", "Death Note", "Bleach" , "Mob Psycho 100" , "Vinland Saga",  "Re:Zero - Starting Life in Another World" , "Sword Art Online" ,"Hunter x Hunter" , "The fragnant flower blooms with dignity" , "Boruto"]

great_anime_list = [ "Death Note" , "One Piece" , "Bleach" , "Dragon Ball Z" , "Re:Zero - Starting Life in Another World" , "Sword Art Online" , "Attack on Titan" , "Fullmetal Alchemist: Brotherhood" , "Hunter x Hunter"  , "Your Lie in April"  , "Made in Abyss" , "Mob Psycho 100" , "Vinland Saga" , "Paranoia Agent" , "Monster" , "Death Parade" , "Hellsing Ultimate" , "Black Clover" , "Fairy Tail" , "Blue Exorcist" , "Noragami" ,"Sword Art Online: Alicization - War of Underworld" , "Tokyo Revengers" , "Dororo" ,"Naruto","Demon Slayer", "Jujutsu Kaisen" , "Tokyo Ghoul" , "Your Name" , "Weathering with You", "A Silent Voice", "5 Centimeters per Second","The fragnant flower blooms with dignity"]

trash_list = ["Rent-a-girlfriend" , "Boruto" ,"My Hero Academia"]

for anime in anime_0['also_loves'] :
    if anime in great_anime_list :
        anime_0["viewers_aura"] = anime_0["viewers_aura"] + 999
    elif anime in trash_list :
        anime_0["viewers_aura"] = anime_0["viewers_aura"] - 999

print(f"{anime_0['title']} viewers aura : {anime_0['viewers_aura']}")

# as aura farming is done , let's free up the anime_0 dict a bit
del anime_0["also_loves"]

print(anime_0)

# now that we have deleted the key-value pair , let's see if we can access it
# anime_0['also_loves'] --> throws an error as the key does not exist anymore

viewers_anime_list = anime_0.get('also_loves', "requested key does not exist") # use get method to retrieve a value from a key if there uncertainty about the key's existence , it takes 2 arguments , the first is the key(if the key exists it's value will be returned as the output) and the second is the default value to return if the key does not exist . If default value is not provided , it will return None --> means absence of value .

print(viewers_anime_list)



