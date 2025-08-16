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
    users = load_users()

    print("=== Welcome to Dice Game ===")
    print("[1] Sign Up")
    print("[2] Log In")
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
            return username
        else:
            print("Invalid username or password. Try again.\n")
            return sign_in()
    else:
        print("Invalid choice, try again.\n")
        return sign_in()


history = []
current_user= ''
balance = 0


def action(choice, bet):
    global balance
    sum_h = sum_b = 0
    print("Okay! Go for it!")
    t.sleep(1)
    for die in range (0, choice):
        human = random.randint(1,6)
        t.sleep(1)
        print ("You got: ", human)
        sum_h += human
    t.sleep(1)
    print("\nYour Total Is: ", sum_h)
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


    if sum_h > sum_b:
        result = "\n✅ You Win!"
        balance += bet
        print(f"You won ${bet}! Current profit: ${balance}")
    elif sum_h < sum_b:
        result = "\n❌ I Win!"
        balance -= bet
        print(f"You lost ${bet}. Current profit: ${balance}")
    else:
        result = "\n😐 It's a Tie (no money lost)."
        print(f"No change in balance. Current profit: ${balance}")


    score_total = (f"Your total was {sum_h}\nMy total was {sum_b}{result}\n\n")


    with open(f"{current_user}_history.txt", "a", encoding="utf-8") as file:
        file.write(score_total)

def rolling():
    global balance
    while True:
        bet = money()
        try:
            choice = int(input("How many dice do you want to roll? (1-3): "))
            if 1 <= choice <= 3:
                action(choice, bet)
            else:
                print("Please enter a valid choice (1-3).")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        while True:
            roll = input("Do you want to continue? (yes/no): ").strip().lower()
            
            if roll == "no":
                print("\n=== Game Over ===")
                if balance > 0:
                    print(f"🎉 You finished with a profit of ${balance}!")
                elif balance < 0:
                    print(f"💸 You finished with a loss of ${-balance}.")
                else:
                    print("😐 You broke even.")
                return 
            
            elif roll == "yes":
                break 
            
            else:
                print("Invalid input. Please enter exactly 'yes' or 'no'.")



def money():
    while True:
        try:
            bet = int(input("How much money do you want to bet? ($100-1000) "))
            if 100 <= bet <= 1000:
                return bet
            else:
                print("The bet must be between 100 and 1000 dollars.")
        except ValueError:
            print("Please enter a valid number.")


def show_previous_history():
    User_name = f"{current_user}_history.txt"
    try:
        with open(User_name, "r") as file:
         print(f"\n== Your Previous Game History ===")
         print(file.read())
    except FileNotFoundError:
         print("f\nNo previous game history found for this user.")  


if __name__ == '__main__':
    current_user = sign_in()
    rolling()