import random
import time as t
from datetime import datetime
import json
import os


USER_FILE = "users.json"


def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}


def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)


def sign_in():
    global current_user
    users = load_users()


    print("=== Welcome to Dice Game ===")
    print("Pick Number 1 or 2")
    print("1. Sign Up")
    print("2. Log In")


    choice = input("Select option: ").strip()


    if choice == "1":
        username = input("Create username: ").strip()
        if username in users:
            print("Username already exists! Please log in instead.")
            return sign_in()


        password = input("Create password: ").strip()
        users[username] = password
        save_users(users)
        print("Account created! You can now log in.")
        return sign_in()


    elif choice == "2":
        username = input("Username: ").strip()
        password = input("Password: ").strip()


        if username in users and users[username] == password:
            print(f"Welcome back, {username}!")
            return True
        else:
            print("Invalid username or password. Try again.\n")
            return sign_in()


    else:
        print("Invalid choice, try again.\n")
        return sign_in()

history = []
current_user= ''


def action(num_dice):
    sum_h = sum_b = 0
    print("Okay! Go for it!")
    for _ in range(num_dice):
     roll = random.randint(1, 6)
     print(f"You rolled: {roll}")
    sum_h += roll
    print(f"Your total: {sum_h}\n")

    print("Computer's turn:")
    for _ in range(num_dice):
        roll = random.randint(1,6)
        print(f"Computer rolled:{roll}")
        sum_b +=roll
        print(f"Computer total:{sum_b}\n")
    
    if sum_h>sum_b:
        print("You win this round!")
    elif sum_h < sum_b:
        print("Computer wins this round!")
    else: 
        print("It's a tie this round!")
    return sum_h,sum_b




    for die in range (0,choice):
        bot=random.randint(1,6)
        t.sleep(1)
        print("I got: ", bot)
        sum_b += bot
    t.sleep(1)
    print("\nMy Total Is: ", sum_b)
    t.sleep(2)

    result = "\nYou Win" if sum_h > sum_b else "\nI Win" if sum_h < sum_b else "\nIt's a Tie"
    print(result)
    t.sleep(1) 

    score_total = (f"Your total was {sum_h}\nMy total was {sum_b}{result}\n\n")
    
    with open("History_File", "a") as file:
        file.write(score_total)



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

    print("Do you want to continue? (yes/no)")
    while roll !="Yes":
        roll = input().lower().capitalize()
        if roll == "Yes":
            rolling()
        else:
            print("It was nice playing with you! Bye!")
            break


def roll_dice(num_dice):
   total = 0
   for _ in range(num_dice):
       roll = random.randint(1, 6)
       print(f"Rolled: {roll}")
       total += roll
   return total

def game():
    print("\n=== Let's Start the game! ===")
    balance = 0
    while balance < 100:
        try:
            balance = int(input("Enter your starting deposit (minimum $100): "))
            if balance < 100:
                print("Deposit must be at least $100.")
        except ValueError:
            print("Please enter a valid number.")

    total_won = 0
    total_lost = 0
    round_number = 1

    while balance > 0:
        print(f"\nRound {round_number} - Current balance: ${balance}")

        # Betting
        bet = 0
        while True:
            try:
                bet = int(input(f"Enter your bet amount (max ${balance}): "))
                if bet < 100 or bet > balance:
                    print(f"Bet must be at least $100 and no more than your current balance (${balance}).")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

        # Choose dice
        num_dice = 0
        while True:
            try:
                num_dice = int(input("How many dice do you want to roll? (1-3): "))
                if 1 <= num_dice <= 3:
                    break
                else:
                    print("You can only roll between 1 and 3 dice.")
            except ValueError:
                print("Please enter a valid number.")

        # Roll and compare
        player_total, computer_total = action(num_dice)  
       
        if player_total > computer_total:
            balance += bet
            total_won += bet
            print(f"You won ${bet}!")
        elif player_total < computer_total:
            balance -= bet
            total_lost += bet
            print(f"You lost ${bet}!")
        else:
            print("It's a tie! No money lost or won.")

        print(f"New balance: ${balance}")
        round_number += 1

        # Continue?
        if balance > 0:
            cont = input("Do you want to continue playing? (yes/no): ").strip().lower()
            if cont != "yes":
                break

    print("\nGame over!")
    print(f"Total won: ${total_won}")
    print(f"Total lost: ${total_lost}")
    print(f"Final balance: ${balance}")
def show_previous_history():
    filename = f"{current_user}_history.txt"
    try:
        with open(filename, "r") as file:
            print(f"\n== Your Previous Game History ===")
            print(file.read())
    except FileNotFoundError:
        print("\nNo previous game history found for this user.")

if __name__ == '__main__':
    if sign_in():
        game()