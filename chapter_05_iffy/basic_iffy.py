# Python uses True or False "value" / boolean expressions to decide which block of code to run
ronaldo_and_messi_are_goats = True

# '=' is assignment, '==' is equality check . Thus we can state that "=" is a statement and "==" is an expression / a query

harry_maguire_is_the_goat = True
antony_is_not_the_BOAT = False

print("harry maguire" < "the goat antony") # always cz antony is the OG
# comparison of strings is basically done lexicographically , i.e. based on the unicode value of each character in the string

# use lower case to ensure uniqueness of datasets , which restrains datasets from being different just by case also ensures a quality of life
best_spideramn = "Bully_Maguire"
print(best_spideramn.lower() == "bully_maguire") # the .lower() method kind of returns a new string datatype value with all characters in lower case , but it doesn't actually change the original one which is stored as the state of "Bully_Maguire" object when we declared it

# numerical comparison
benzema = 15

if benzema > 15 :
  print("armageddon")
elif benzema <= 15 and not antony_is_not_the_BOAT : # yah , in python the negate operator is 'not' , not '!' like in C/C++
  print("That's why they're the GOATz ... The GOoAAaaTTTziess !!! ")
elif ronaldo_and_messi_are_goats or harry_maguire_is_the_goat :
  print("The OG Aura farmers ...")
else :
  print("That's why he is the GOAT ... The GOoAAaaTTT !!! ")

# searching in a list
goated_players = ["ronaldo", "messi", "benzema", "maguire", "antony" , "nicholas"]


if "onana" in goated_players :
  print("As expected ...")
elif not("onanna"  in goated_players and "nicholas"  in goated_players) :
  print("Faulty list ...")
elif "onana" or "nicholas" not in goated_players :
  print("also true condition ...") # it's true cz in py it's interpreted as "onana" or ("nicholas" not in goated_players) , which is always true as "onana" is a string and non-empty strings are always truthy . But this block won't get executed as the previous one is also true and thus the interpreter will not check this one and move on by getting out of the if-elif-else block

# This is important cz in a if-elif-else chain , if a condition is met that block executes and the code flow executes that block . Thus , if multiple conditions are true , only the first one will be executed and the rest will be ignored .

# So , if multiple conditions needed to be checked , use multiple "independent" iffy chains . 

