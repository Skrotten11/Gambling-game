import random as r
import time

#Values---------------------------------------------
currency = 100
version = 1.1
#Start------------------------------------------------------
print("Welcome to the gambling game!")
print(f"Current currency: {currency}")
print(f"Version {version}")
print("---------------------------------------------")

#Gamemodes----------------------------------------------------------------------

def fifty():
    global currency
    bet = int(input("Enter Bet"))
    currency = currency - bet
    choice = int(input("Enter number (1, 2)"))
    numberVLU = r.randint(1, 2)
    time.sleep(2)
    print(f"Landed on: {numberVLU}")

    if numberVLU == 1:
        if choice == 1:
            print("You win!!")
            currency = currency + bet * 2
            print(f"Your currency: {currency}")
        if choice == 2:
            print("You lose!")
            print(f"Your currency: {currency}")
    if numberVLU == 2:
        if choice == 2:
            print("You win!!")
            currency = currency + bet * 2
            print(f"Your currency: {currency}")
        if choice == 1:
            print("You lose!")
            print(f"Your currency: {currency}")
    print("---------------------------------------")
    print("")
    if currency < 1:
        print("You lose!")
        time.sleep(3)
        exit()
    Choose()




def twenty():
    global currency
    bet = int(input("Enter Bet"))
    currency = currency - bet
    choice = int(input("Enter number (1, 2, 3, 4, 5)"))
    numberVLU = r.randint(1, 5)
    time.sleep(2)
    print(f"Landed on: {numberVLU}")
    
    if numberVLU == 1:
        if choice == 1:
            print("You win!!")
            currency = currency + bet * 5
            print(f"Your currency: {currency}")
        else:
            print("You lose!")
            print(f"Your currency: {currency}")

    if numberVLU == 2:
        if choice == 2:
            print("You win!!")
            currency = currency + bet * 5
            print(f"Your currency: {currency}")
        else:
            print("You lose!")
            print(f"Your currency: {currency}")

    if numberVLU == 3:
        if choice == 3:
            print("You win!!")
            currency = currency + bet * 5
            print(f"Your currency: {currency}")
        else:
            print("You lose!")
            print(f"Your currency: {currency}")

    if numberVLU == 4:
        if choice == 4:
            print("You win!!")
            currency = currency + bet * 5
            print(f"Your currency: {currency}")
        else:
            print("You lose!")
            print(f"Your currency: {currency}")

    if numberVLU == 5:
        if choice == 5:
            print("You win!!")
            currency = currency + bet * 5
            print(f"Your currency: {currency}")
        else:
            print("You lose!")
            print(f"Your currency: {currency}")

    print("---------------------------------------")
    print("")
    if currency < 1:
        print("You lose!")
        time.sleep(3)
        exit()

    Choose()



def ten():
    global currency
    bet = int(input("Enter Bet"))
    currency = currency - bet
    choice = int(input("Enter number (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"))
    numberVLU = r.randint(1, 10)
    time.sleep(2)
    print(f"Landed on: {numberVLU}")
    if numberVLU == 1:
        if choice == 1:
            print("You win!!")
            currency = currency + bet * 10
            print(f"Your currency: {currency}")
        else:
            print("You lose")
            print(f"Your currency: {currency}")
            
    if numberVLU == 2:
        if choice == 2:
            print("You win!!")
            currency = currency + bet * 10
            print(f"Your currency: {currency}")
        else:
            print("You lose")
            print(f"Your currency: {currency}")

    if numberVLU == 3:
        if choice == 3:
            print("You win!!")
            currency = currency + bet * 10
            print(f"Your currency: {currency}")
        else:
            print("You lose")
            print(f"Your currency: {currency}")

    if numberVLU == 4:
        if choice == 4:
            print("You win!!")
            currency = currency + bet * 10
            print(f"Your currency: {currency}")
        else:
            print("You lose")
            print(f"Your currency: {currency}")

    if numberVLU == 5:
        if choice == 5:
            print("You win!!")
            currency = currency + bet * 10
            print(f"Your currency: {currency}")
        else:
            print("You lose")
            print(f"Your currency: {currency}")

    if numberVLU == 6:
        if choice == 6:
            print("You win!!")
            currency = currency + bet * 10
            print(f"Your currency: {currency}")
        else:
            print("You lose")
            print(f"Your currency: {currency}")

    if numberVLU == 7:
        if choice == 7:
            print("You win!!")
            currency = currency + bet * 10
            print(f"Your currency: {currency}")
        else:
            print("You lose")
            print(f"Your currency: {currency}")

    if numberVLU == 8:
        if choice == 8:
            print("You win!!")
            currency = currency + bet * 10
            print(f"Your currency: {currency}")
        else:
            print("You lose")
            print(f"Your currency: {currency}")

    if numberVLU == 9:
        if choice == 9:
            print("You win!!")
            currency = currency + bet * 10
            print(f"Your currency: {currency}")
        else:
            print("You lose")
            print(f"Your currency: {currency}")

    if numberVLU == 10:
        if choice == 10:
            print("You win!!")
            currency = currency + bet * 10
            print(f"Your currency: {currency}")
        else:
            print("You lose")
            print(f"Your currency: {currency}")

    print("---------------------------------------")
    print("")
    if currency < 1:
        print("You lose!")
        time.sleep(3)
        exit()
    Choose()
#Choose game type function--------------------------------------------------------
def Choose():
    print("Gamemodes:")
    print("50/50 (There is a 50% chance your bet doubles)")
    print("20/80 (There is a 20% chance your bet gets multiplied X5")
    print("10/90 (There is a 10% chance your bet gets multiplied X10")
    game = input("I want to play: ")
    if game == "50/50":
        fifty()
    elif game == "20/80":
        twenty()
    elif game == "10/90":
        ten()
    else:
        print("Invalid gamemode, try again!")
        print("")
        Choose()

Choose()






                
