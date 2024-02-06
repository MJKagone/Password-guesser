"""
A program to test how long it takes to break a given password with lookup tables and brute force.
1) Checks the most common passwords worldwide and in Finland, as well as names and surnames.
2) Checks all combinations of digits.
3) Checks all combinations of digits and extended ASCII characters.

The used lookup tables can be found at:
-https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials (most common passwords)
-https://wiki.skullsecurity.org/index.php/Passwords (Finnish passwords)
-https://github.com/zeraye/names-surnames-list (names)
-https://github.com/dwyl/english-words (English words)
-https://github.com/hugovk/everyfinnishword (Finnish words)
Of course, you may also choose to use different files or omit this step entirely.
"""

from itertools import product
from numpy import loadtxt
from numpy import char
from time import time

n = 8 # maximum number of characters in password

def check_tables(password):
    """
    Check if the given password exists in various tables of common passwords and names.

    Parameters:
        password (str): The password to be checked.

    Returns:
        bool: True if the password is found in any of the tables, False otherwise.
    """

    global_passwords = loadtxt("10-million-password-list-top-1000000.txt", dtype=str)
    male_names = char.lower(loadtxt("male-names-list.txt", dtype=str))
    female_names = char.lower(loadtxt("female-names-list.txt", dtype=str))
    surnames = char.lower(loadtxt("surnames-list.txt", dtype=str))
    finnish_passwords = loadtxt("alypaa.txt", dtype=str) # the best I could find
    english_words = loadtxt("words.txt", dtype=str)
    finnish_words = loadtxt("kaikkisanat.txt", dtype=str) # have to do some cleaning in the file for it to work

    print("1) Checking the most common passwords worldwide and in Finland")
    if (password in global_passwords or 
        password in finnish_passwords or 
        password in male_names or 
        password in female_names or 
        password in surnames or
        password in english_words or
        password in finnish_words or
        password in char.capitalize(male_names) or
        password in char.capitalize(female_names) or
        password in char.capitalize(surnames) or
        password in char.capitalize(english_words) or
        password in char.capitalize(finnish_words)):
            return True
    return False
      

def check_digits(password):
    """
    Checks if the given password matches any combination of digits.

    Parameters:
        password (str): The password to be checked.

    Returns:
        bool: True if the password matches any combination, False otherwise.
    """

    digits = "0123456789"
    print("2) Checking all digits up to")
    for length in range(1, n+1):
        print("...%d characters" % length)
        for combination in product(digits, repeat=length):
            test = ''.join(combination)
            if test == password:
                return True
    return False


def check_digits_and_extended_ASCII(password):
    """
    Checks if the given password matches any combination of digits and extended ASCII characters.

    Parameters:
        password (str): The password to be checked.

    Returns:
        bool: True if the password matches any combination, False otherwise.
    """
        
    characters = "0123456789abcdefghijklmnopqrstuvwxyzåäöüABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖÜ!\"#$€%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    print("3) Checking all digits and extended ASCII up to")
    for length in range(1, n+1):
        print("...%d characters" % length)
        for combination in product(characters, repeat=length):
            test = ''.join(combination)
            if test == password:
                return True
    return False
    

def main():
    """
    Prompts the user for a password and applies the above functions to it.
    Also measures the time taken.
    """

    password = input("Enter a password to test: ")
    start = time()

    if check_tables(password):
        duration = time() - start
        if duration < 60:
            print("Password '" + password + "' found in " + "%.1d s" % duration)
        else:
            print("Password '" + password + "' found in " + "%.1d min %.1d s" % (duration//60, duration%60))

    elif check_digits(password):
        duration = time() - start
        if duration < 60:
            print("Password '" + password + "' found in " + "%.1d s" % duration)
        else:
            print("Password '" + password + "' found in " + "%.1d min %.1d s" % (duration//60, duration%60))

    elif check_digits_and_extended_ASCII(password):
        duration = time() - start
        if duration < 60:
            print("Password '" + password + "' found in " + "%.1d s" % duration)
        else:
            print("Password '" + password + "' found in " + "%.1d min %.1d s" % (duration//60, duration%60))
    else:
        print("Password not found. Program halted after exhausting all possibilities.")


if __name__ == "__main__":
    main()
