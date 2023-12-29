from game_logic import bet
from decouple import config

my_money = config('MY_MONEY',cast=int)


while True:
    print('Your balance' + str(my_money))
    print('Start casino ? (yes or no)')
    a = input('')
    if a == 'no':
        print("You exit from casino")
        break
    elif a == 'yes':
        b = int(input('Choose number from 1 to 30'))
        g = int(input('How much you want to bet ?'))
        my_money -= g
        my_money += bet(b,g)
    else:
        print('Error,try again')
