"""Get password and print the asteriks of password length"""

"""Constants"""
MIN_PASS_LENGTH = 5


def main():
    """Main function"""
    geta_password = get_pwd()
    asteriks = get_asteriks(geta_password)
    print(asteriks)


def get_pwd():
    geta_password = input("Enter password: ")
    while len(geta_password) < 5:
        print(f"Invalid. Minimum password length is {MIN_PASS_LENGTH}.")
        geta_password = input("Enter password: ")
    return geta_password


def get_asteriks(geta_password):
    asteriks = '*' * len(geta_password)
    return asteriks


main()
