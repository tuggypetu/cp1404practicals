"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password), password))


def is_valid_password(password):
    """Determine if the provided password is valid."""

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    # TODO: if length is wrong, return False
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    if not SPECIAL_CHARS_REQUIRED:
        count_special = 11111

    if count_digit > 0 and count_upper > 0 and count_lower > 0 and count_special > 0 and 5 <= len(password) <= 15:
        return True
    else:
        print("Invalid password!")
        print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
              "characters, and contain:")
        print("\t1 or more uppercase characters")
        print("\t1 or more lowercase characters")
        print("\t1 or more numbers")
        if SPECIAL_CHARS_REQUIRED:
            print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
        return False


main()
