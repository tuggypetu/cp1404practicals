
MIN_LENGTH = 5
MAX_LENGTH = 15


password_check = input("Enter password: ")
for i in password_check:
    if i.isdigit():
        print("true")
    else:
        print("false")
