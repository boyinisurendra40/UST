1.
import os


downloads_folder = os.path.expanduser("~/Downloads")
for item in os.listdir(downloads_folder):
    item_path = os.path.join(downloads_folder, item)
    if os.path.isfile(item_path):
        print(f"{item} - File")
    elif os.path.isdir(item_path):
        print(f"{item} - Folder")
    else:
        print(f"{item} - Unknown")

2.
import string
leters=string.ascii_letters
print("Ascii letters:",leters)


3.
from random import sample
from string import ascii_letters
five=sample(ascii_letters,5)
print(five)

4.
from datetime import datetime, timedelta

def six_months_later(current_date):
    return current_date + timedelta(days=30*6)

user_input = input("Enter the date (DD/MM/YYYY): ")

input_date = datetime.strptime(user_input, "%d/%m/%Y")

formatted_date = input_date.strftime("%A %d %B %Y")
print("Formatted date:", formatted_date)

day_of_week = input_date.strftime("%A")
print("Day of the week:", day_of_week)

new_date = input_date + timedelta(days=15, hours=23)
print("New date after adding 15 days and 23 hours:", new_date.strftime("%d/%m/%Y %H:%M:%S"))

current_date = datetime.now()
date_six_months_later = six_months_later(current_date)
print("Date 6 months from today:", date_six_months_later.strftime("%d/%m/%Y"))


5.
import random

def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
        return "user"
    else:
        return "computer"

while True:
    user_input = input("Enter rock, paper, or scissors: ").lower()

    if user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid input! Please enter rock, paper, or scissors.")
        continue

    comp_input = computer_choice()
    print(f"Computer chose: {comp_input}")

    result = determine_winner(user_input, comp_input)

    if result == "draw":
        print("It's a draw! Let's continue the game.")
    elif result == "user":
        print("You win!")
        break
    else:
        print("Computer wins!")
        break

