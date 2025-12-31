""" import random
import string

print("🔐 Password Generator")

# Get password length from user
length = int(input("Enter password length: "))

# Characters to use in password
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = lowercase + uppercase + digits + symbols

# Generate password
password = ""
for i in range(length):
    password += random.choice(all_characters)

print("Generated Password:", password)


import random 
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbols ='!@#$%^&*()_+{}[]:;,.<>?/|'

all_charts = lower + upper + number + symbols
length = int(input("Enter the length of password:"))

password = ''.join(random .sample (all_charts, length))
print("Your password is:", password)"""


import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbols = '!@#$%^&*()_+{}[]:;,.<>?/|'

all_chars = lower + upper + number + symbols

command = input("Type 'password generator' to continue: ").lower()

if command == "password generator":
    try:
        length = int(input("Enter the length of password: "))

        if length <= 0:
            print("Password length must be greater than 0")
        elif length > len(all_chars):
            print("Password length too long")
        else:
            password = ''.join(random.sample(all_chars, length))
            print("Your password is:", password)

    except ValueError:
        print("Please enter a valid number")

else:
    print("Invalid command. Program stopped.")

