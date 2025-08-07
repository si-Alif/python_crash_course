# 7.1
car = input("Which car would you like to rent ? ")

print(f"let me see if I can find you a {car}")

# 7.2
customer_count = int(input("How many people are in your dinner group ? "))

if customer_count <= 8 :
    print("Your table is ready")
else :
    print("sorry , you'll have to wait for a table")

# 7.3
num = int(input("Enter a number : "))

if num % 10 == 0 :
    print("Multiple of 10")
else :
    print("Not a multiple of 10")


# 7.4

topping_message = "Enter the topping you Want(Enter 'quit' to exit) : "

topping_needed = True # 7.6

while topping_needed :
    topping = input(topping_message)
    if(topping.lower() == 'quit') :
        topping_needed = False
        # break --> 7.6
    else :
        print(f"I'll add {topping} to your pizza")

# 7.5

total_customer_in_line = 5

while total_customer_in_line > 0 : # 7.6
    age = int(input("Enter your age : "))
    if age <= 3 :
        print("\tFree")
    elif age > 3 and age <= 12 :
        print("\t$10")
    else :
        print("\t$15")
    total_customer_in_line -= 1

#  7.7
# while True :
#     print("Infinite loop ... press CTRL + R  to exit ")

# 7.8
to_be_prepared = ["tuna sandwich" , "steak sandwich" , "pastrami sandwich" ,"grilled cheese sandwich" , "chicken sandwich" , "pastrami sandwich" , "pastrami sandwich"]

order_list = to_be_prepared.copy() # be aware that if you don't give a copy of to_be_prepared list in order_list , then as the to_be_prepared list and order_list refers to the same object , to-be-prepared list object's state will also change
order_list.reverse()

prepared_list = []

while order_list :
    prepared = order_list.pop()
    print(f"Prepared {prepared}")
    prepared_list.append(prepared)

for prepared in prepared_list :
    print(prepared)

# 7.9
print("We ran out of pastrami")

while "pastrami sandwich" in to_be_prepared :
    to_be_prepared.remove("pastrami sandwich")

for to_prepare in to_be_prepared :
    print(to_prepare)

7.10

wishlist = {}


while True :
    name = input("Enter your name( to exit enter 'quit') : ")
    if name == 'quit' :
        break
    else :
        wish = input("Enter your dream travel destination : ")
        wishlist[name] = wish

for name , place in wishlist.items() :
    print(f"{name} wants to visit {place}")