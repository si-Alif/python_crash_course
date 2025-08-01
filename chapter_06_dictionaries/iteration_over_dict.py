fav_lan = {
    'Alice': 'Python',
    'Bob': 'Java',
    'Charlie': 'JavaScript',
    'Diana': 'C++',
    'Eve': 'Ruby',
}

lan_list = fav_lan.items()  # Returns a set like view object of the dictionary's items , here each element of list looks like (<key> , <value>)

print(lan_list)

for name , lan in lan_list : # Here the 1st variable works as the binding of key and the second for it's value when the iteration id going on
    print(f"{name}'s favorite language is {lan}.")

# suppose we only want to print the keys
for name in fav_lan :
    print(name)

# or we can do the same thing using the keys() method
for key in fav_lan.keys() : # returns a view object that displays a list of all the keys in the dictionary
    print(key)

for _ , lan in fav_lan.items(): # Here we are using underscore to ignore the key, as we only want the value
    print(f"One of the favorite languages is {lan}.")

# kinda easier way
for lan in fav_lan.values() : # returns all value list , "all of them"
    print(f"{lan} language is mentioned")

# as we saw , <list>.values() returns all the values and doesn't care about the uniqueness of values . To solve this , we can put all the values in a set data structure set(<list>) , which ensures that each value in it is "Unique"

fav_lan['sarah'] = "C++"
fav_lan['joe'] = "Java"

unique_lan = set(fav_lan.values())
for unique_lan in unique_lan :
    print(f"Uniquely mentioned language : {unique_lan}")


#  more about set : if you want to initialize a set value , use {} which will only contain value , no key value pair unlike dict and wrapped in {} unlike list

st = {"zoro" , "luffy" , "nami" , "zoro"}
st.add("sanji")
print(st) # only unique items

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

# sorting in python --> sorted doesn't manipulate the original data rather returns a sorted order of the OG , meanwhile <list>.sort() changes the OG data which works as destructive
# both of them use Timsort as the sorting principal



