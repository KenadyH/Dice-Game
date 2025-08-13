import random
import time as t


def action(choice):
    sum_h = sum_b = 0
    print("Okay! Go for it!")
    t.sleep(1)
    for die in range (0, choice):
        human = random.randint(1,6) 
        t.sleep(1)
        print ("You got: ", human)
        sum_h += human
    t.sleep(1)
    print("\n Your Total Is: ", sum_h)
    t.sleep(1)
    print("\nNow it's my turn")
    t.sleep(1)

    for die in range (0,choice):
        bot=random.randint(1,6)
        t.sleep(1)
        print("I got: ", bot)
        sum_b += bot
    t.sleep(1)
    print("\nMy Total Is: ", sum_b)
    t.sleep(2)

    result = "\n You Win" if sum_h > sum_b else "\nI Win" if sum_h < sum_b else "\n It's a Tie"
    print(result)
    t.sleep(1) 


def rolling():
    die= 0
    roll = " "
    while die==0:
        choice = int(input("How many dice do you want to roll? (1-3) "))
        if choice>0 and choice<4:
            action(choice)
            break
        else:
            print("Please enter a valid choice.")

    print("Do you want to continue? (yes/no")
    while roll !="Yes":
        roll = input().lower().capitalize()
        if roll == "Yes":
            rolling()
        else:
            print("It was nice playing with you! Bye!")
            break

def money():
    while true:
        try:
            money = int(input("How much money do you want to bet? (100<1000) "))
            if 100 <= money <= 1000:
            print('The minimum bet is 100 dollars.')
            except ValueError:
            print("You have to bet 100 dollars or more.")
                return money 
            print(f"You have {enter money:}"good luck!")
    if result=="Win":
        print("You won! Would you like to bet again? (yes/no) ")
        elif result=="Lose":
        print("You lost! Would you like to bet again? (yes/no) ")
        if =="yes"
        add more money()
        if no
        else:
            print("Thanks for playing! Goodbye!")
            
        
        

        
            






if __name__ == '__main__':
    rolling()