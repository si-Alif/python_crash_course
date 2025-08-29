from random import choices

lottery_content = (
  1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 'a' , 'b' , 'c' , 'd' , 'e'
)

print(f"any 4 numbers out these : { choices(lottery_content , k=4)} \n\t will be considered as a winner")

