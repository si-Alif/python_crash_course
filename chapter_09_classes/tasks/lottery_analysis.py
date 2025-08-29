from random import choice

lottery_content = (
  1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 'a' , 'b' , 'c' , 'd' , 'e'
)

my_ticket = choice(lottery_content)

chance = 1

while True :
  winner = choice(lottery_content)
  if winner == my_ticket :
    break
  else :
    chance += 1

print(f"It took me {chance} tries to win the lottery")