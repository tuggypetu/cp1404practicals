"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

import doctest

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
    """
    Determine if the provided password is valid.
    >>> is_valid_password('hello')
    False
    >>> is_valid_password('It is an ex parrot.')
    False
    >>> is_valid_password('omg, why you so dumb? Idk')
    False
    >>> is_valid_password('Tuggy@1')
    True
    >>> is_valid_password('Tuggy@1sgsgsgsgsgsgsgsgsggggggggggg')
    False
    >>> is_valid_password('tuggy@1sgsgs')
    False
    >>> is_valid_password('Tuggy1sgsgs')
    False
    >>> is_valid_password('Tuggy@sgsgsgsg')
    False
    """

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

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
        # print("Invalid password!")
        # print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
        #       "characters, and contain:")
        # print("\t1 or more uppercase characters")
        # print("\t1 or more lowercase characters")
        # print("\t1 or more numbers")
        # if SPECIAL_CHARS_REQUIRED:
        #     print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
        return False


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert is_valid_password('yolo1ee') is False
    assert is_valid_password("Python") is False
    assert is_valid_password("hi") is False
    assert is_valid_password('Tuggy@1') is True


run_tests()
# doctest.testmod()
# main()
