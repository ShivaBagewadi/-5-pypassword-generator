import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# easy level

# password = ""
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# for char in range(0,nr_letters):
#     password += random.choice(letters)
#
# for num in range(0,nr_numbers):
#     password += random.choice(numbers)
#
# for sym in range(0,nr_symbols):
#     password += random.choice(symbols)
#
# print(password)

# hard level

password_ist = []
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for char in range(0,nr_letters):
    password_ist.append(random.choice(letters))

for num in range(0,nr_numbers):
    password_ist += random.choice(numbers)

for sym in range(0,nr_symbols):
    password_ist.append(random.choice(symbols))

print(password_ist)

random.shuffle(password_ist)
print(password_ist)
char = ""
for password in password_ist:
    char += password

print(f"Your password is: {char}")
