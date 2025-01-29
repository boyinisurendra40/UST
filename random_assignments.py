#Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5

import random
random_num=[random.choice(range(100,999,5)) for _ in range(3)]
print("randon numbers divisible by 5=",random_num)

#Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.

import random
lottery=[random.randint(1000,9999) for _ in range(100)]
winner=random.sample(lottery,2)
print("winners=",winner)

#Exercise 3: Generate 6 digit random secure OTP
import random
import string
otp=random.randit(1000,9999)
print("otp=",otp) 

Exercise 4: Pick a random character from a given String
import random
random_char=input("enter string=")
ch=random.choice(random_char)
print("random charcter=",ch)

Exercise 5: Generate random String of length 5
import random
import string
random_string=''.join(random.choice(string.ascii_letters)for _ in range(6))
print("Random string of length 5=",random_string)



Exercise 6: Generate a random Password which meets the following conditions Password length must be 10 characters long.
It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

import random
import string
def generate_password():
    upper_letters = random.choices(string.ascii_uppercase, k=2)
    digits = random.choices(string.digits, k=1)
    special_chars = random.choices("!@#$%^&*()", k=1)
    other_chars = random.choices(string.ascii_letters + string.digits + "!@#$%^&*()", k=6)
    
    password = upper_letters + digits + special_chars + other_chars
    random.shuffle(password)
    
    return ''.join(password)

print("Random Password:", generate_password())
    


#Exercise 7: Calculate multiplication of two random float numbers
import random

float1 = random.uniform(1.0, 10.0)
float2 = random.uniform(1.0, 10.0)

product = round(float1 * float2, 2)

float1 = round(float1, 2)
float2 = round(float2, 2)

print(f"Multiplication: {float1} * {float2} = {product}")


#Exercise 8: Generate random secure token of 64 bytes and random URL
import random
import string

secure_token = ''.join(random.choices(string.hexdigits, k=64))
random_url = f"https://example.com/{''.join(random.choices(string.ascii_letters + string.digits + '-_', k=16))}"

print("Secure Token:", secure_token)
print("Random URL:", random_url)


#Exercise 9: Roll dice in such a way that every time you get the same number
import random

random.seed(10)  # Fixing the seed for reproducibility
dice_roll = random.randint(1, 6)

print(f"Dice Roll: {dice_roll}")

Exercise 10: Generate a random date between given start and end dates

import random
from datetime import datetime, timedelta

start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 1, 1)

delta = end_date - start_date
random_days = random.randint(0, delta.days)
random_date = start_date + timedelta(days=random_days)

print("Random Date:", random_date.strftime('%Y-%m-%d'))














