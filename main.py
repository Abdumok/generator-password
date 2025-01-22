import string
import random
# ask user for the password length and the length of every content

letters_len=0
numbers_len=0
symbols_len=0
password_len = int(input("Enter the length of the password: "))
# check for the password length against the sum of the user inputs:
while password_len != (letters_len + numbers_len + symbols_len):

    letters_len = int(input("Enter the number of letters: "))
    numbers_len = int(input("Enter the number of numbers: "))
    symbols_len = int(input("Enter the number of symbols: "))
    print("Invalid inputs, the sum of the letters,numbers and symbol don't match the password length")






