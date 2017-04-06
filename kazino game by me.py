import random
#1. user has money - 100 dollars - variable +

#2. user inputs black or red in while loop+

#3. user plays roullette and bets black or red(compare in if)+

#3.5 casino says: what color won and if the user wins or not

#4if user guesses the color he get 10 dollar if not he looses 10 dollar+

#5 if user has 0 dollars while breaks+

#print(random.randint(0,1))# 0 menas red 1 means black

money=100
user_bet_int = 0
while (money>0):
    color=input("What color? b for Black or r for Red?")
    if(color=='b'):
        user_bet_int = 1
    else:
        user_bet_int = 0
    ball_roll = random.randint(0, 1)
    print ("winner is ...(0 is red, 1 is black ) ", ball_roll)
    if (ball_roll==user_bet_int):
        money=money+10
        print("You Win !!")
    else:
        money=money-10
        print("You Lost!")
    print('Your bank is ', money)
    print('\n\n\n\n\n')






