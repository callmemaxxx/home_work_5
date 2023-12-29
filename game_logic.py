import random
import time

def bet(b,g):
    print("Please wait...")
    time.sleep(2)


    choice = random.randint(1,31)
    if choice == b:
        print(choice)
        print("You WIN!")
        return g * 2
    else:
        print(choice)
        print(f'-{g}$')
        print("You can try again")
        return 0