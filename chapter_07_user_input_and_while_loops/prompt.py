# name = input("Enter your name in title Case : ") # be concise with the prompt to make it clearer to the user what you're looking for as a programmer
# print(f"Hello {name}")

# # prompt message stored in variable
# prompt = "Would you like to participate in our survey ."
# prompt+= "\n\tIf you're willing to , would you mind sharing your name ? "

# name = input(prompt)
# age = input("\tHow old are you ? ") # input always returns a string , be aware of that while dealing with inputs
# dept = input("\tWhat is your department ? ")

# print(f"Thanks for your participation , we really appreciate your feedback {name.title()}")


# age = int(input("How old are you ? ")) # as input is by default string , we need to convert it to int for numerical comparison

# print(f"Your age is {age > 30}")

# #  or you can take the input and then type cast it
# guess = input("Enter a number between 1 and 10 : ")
# guess = int(guess)


# parrot = "Tell me something and I'll repeat it back to you ."
# parrot += "\n\tEnter 'quit' to end the program .\n\t"

# message = input(parrot)

# while message.lower() != "quit" :
#   print(message)
#   message = input(parrot)


isLTR10 = True

target = 7

while isLTR10 :
    guess = int(input("Enter a number between 1 and 10 : "))
    if guess == 10 :
        isLTR10 = False
    elif guess == 7 :
        print("You got it !")
        curr = 1
        while curr < 36:
            if curr == 3 :
                curr += 1 # in while loop you need to manually increment the counter or the "curr" value will stay 3 forever resulting in infinite loop . As for loop does iterator variables incrementation  automatically , there you don't need to do this incrementing manually
                continue
            elif curr == 33 :
                break
            else :
                print(curr)
            curr += 1
    else:
        print("Try again !")


