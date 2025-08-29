from make_car import make_car as Make_Car

# 8.1
def display_message() :
    """Display the current topic of the chapter"""
    print("Functions")

display_message()

# 8.2
def favorite_book(title) :
	"""Display a message about my favorite book"""
	print(f"One of my favorite books is {title.title()}")

favorite_book("meditations")

# 8.3 & 8.4
def design_shirt(size = "medium", msg = "I love Python"):
    """Summarize the shirt that's going to be made"""
    print(f"The size of the shirt is {size} and the message printed on it is {msg}")

design_shirt()
design_shirt("large")
design_shirt(size = "medium", msg = "I love GOlang")

# 8.5
def describe_city(city  , country = "Bangladesh") :
    """Describe a city's location"""
    print(f"{city.title()} is in {country.title()}")

describe_city("Rajshahi")
describe_city("paris" , "france")
describe_city("tokyo" , "japan")

# 8.6
def city_country(city, country):
    """Return a string in the format:
    'City, Country'."""
    return f"{city.title()} , {country.title()}"

print(city_country("Rajshahi", "Bangladesh"))
print(city_country("tokyo", "japan"))
print(city_country("paris", "france"))

# 8.7 & 8.8

def make_album(artist , album , tracks = None):
    """Return a dictionary containing info about an album"""
    return {
        "artist" : artist.title(),
        "album" : album.title(),
        "tracks" : tracks
    }

while True :
    info = []
    print("Enter 'q' to quit")
    artist = input("Enter the name of the artist : ")
    if artist == 'q' :
        break
    else :
        info.append(artist)
    album = input("Enter the name of the album : ")
    if album == 'q' :
        break
    else :
        info.append(album)
    tracks = input("Enter the number of tracks : ")
    if tracks == 'q' :
        break
    else :
        info.append(tracks)

    print(make_album(*info))

# 8.9 , 8.10 & 8.11
messages = [
    "I love programming" ,
    "JS sucks",
    "C is great for learning programming",
    "Python is also great for learning programming",
    "C++ is also great for learning CP",
]

def print_messages(messages) :
    sent_messages = []
    # for message in messages :
    #     print(message)
    #     sent_messages.append(message)
    #     # bug is if you remove one element , other elements from the right side are shifted to left . So , your iterator is moving from 0 to 1 but on the go you're also removing the current element from the list , resulting in removal of the even index elements
    #     messages.remove(message)

    copy = messages[:]
    copy.reverse()
    while copy:
        message = copy.pop()
        print(message)
        sent_messages.append(message)

    print("Message to be send" , messages)
    print("Sent messages" , sent_messages)

print_messages(messages)


# 8.12
def sandwich_items(*items) :
    """Print a summary of the items in a sandwich"""
    print("You ordered a sandwich with following items : ")
    for item in items :
        print(f"\t{item.title()}")

sandwich_items("bacon" , "cheese" , "tomato" , "lettuce")
sandwich_items("bacon" , "cheese" , "tomato")

# 8.13
def build_profile(first , last , **user_info):
    """Build a user info JSON  based on info provided ny the user"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

build_profile("hero" , "alom" , location = "bogura" , field = "arts" , age = 69)


# 8.14
info = Make_Car("subaru" , "outback" , color = "blue" , tow_package = True , doors = 4 , wheel = 4 )

for key , value in info.items():
    print(f"{key} : {value}")

# 8.15

