import string
import random


password_len = int(input("Enter the length of the password: "))

# check for the password length against the sum of the user inputs:
while True:

    # ask user for the length of password contents
    letters_len = input("Enter the number of letters: ")
    numbers_len = input("Enter the number of numbers: ")
    symbols_len = input("Enter the number of symbols: ")

    if not letters_len.isdigit() or not numbers_len.isdigit() or not symbols_len.isdigit():
        print("Invalid input, numbers only are acceptable.")

    elif password_len == ( int(letters_len) + int(numbers_len) + int(symbols_len) ):
        break

    else:
        print("Invalid inputs, the sum of the letters,numbers and symbol don't match the password length")

letters= random.choices(string.ascii_letters, k=int(letters_len))
numbers= random.choices(string.digits, k=int(numbers_len))
symbols= random.choices(string.punctuation, k=int(symbols_len))

password_as_list= letters + numbers + symbols

random.shuffle(password_as_list)

your_password= "".join(password_as_list)

print(f"\nYour new password is: {your_password}")






