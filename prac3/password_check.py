"""Get password and print asteriks of password length"""

MIN_PASS_LENGTH = 5
get_password = input("Enter password: ")
while len(get_password) < 5:
    print(f"Invalid. Minimum password length is {MIN_PASS_LENGTH}.")
    get_password = input("Enter password: ")
print('*' * len(get_password))
