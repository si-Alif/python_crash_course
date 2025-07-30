import random
colors  = ["green", "blue", "red", "yellow", "purple", "orange"]
alien_color = random.choice(colors)

# 5.3
if( alien_color == "green"):
    print("You just earned 5 points!")
else : # 5.4
    print(f"You earned 10 points as you hit a {alien_color} alien!")


# 5.5
alien_color_v2 = random.choice(colors)
if alien_color_v2 == "green":
    print("You just earned 5 points!")
elif alien_color_v2 == "yellow":
    print("You just earned 10 points!")
elif alien_color_v2 == "red":
    print("You just earned 15 points!")


# 5.6
age = random.randint(1, 100) # returns a random integer between the given range where both are inclusive

if age < 2:
    print("baby!")
elif age >= 2 and age < 4:
    print("toddler!")
elif age >= 4 and age < 13:
    print("kid!")
elif age >= 13 and age < 20:
    print("annoying teenager!")
elif age >= 20 and age < 65:
    print("adult!")
elif age >= 65:
    print("elderly!")

# 5.7
favorite_fruits = ["tangerines", "mango", "lichi"]

if "tangerines" in favorite_fruits:
    print("You really like tangerines!")

if "banana" in favorite_fruits:
    print("You really like apples!")

if "apple" in favorite_fruits:
    print("You really like apples!")

if "guava" in favorite_fruits:
    print("You really like guavas!")

if "mango" in favorite_fruits:
    print("You really like mangoes!")

if "lichi" in favorite_fruits:
    print("You really like lichis!")


# 5.8
usernames = ["bob", "alice", "admin", "charlie", "dave"]
# usernames = [] ----> #5.9

if usernames :
    for username in usernames:
        if username == "admin":
            print("Hello admin , would you like to see a status report ?")
        else :
            print(f"Hello {username} , thank you for logging in again ." )
else :
    print("we need to find some users ")


# 5.10

curr_users  = ["bob", "alice", "joe", "charlie", "dave" , "zayed" , "grimmice_shake"]
new_users = ["joe" , "alex" , "awrarrar" , "modi" , "hasina"]

if curr_users and new_users :
    for new_user in new_users :
        if new_user.lower() not in curr_users :
            print(f"username {new_user} is available")
        else :
            print(f"{new_user} has already been used .")


# 5.11
nums = [1, 2,3 ,4, 5, 6, 7, 8, 9]

for num in nums:
    if num == 1:
        print("1st")
    elif(num == 2):
        print("2nd")
    elif (num == 3):
        print("3rd")
    else :
        print(f"{num}th")

