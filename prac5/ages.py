"""Input create dict, then print ages"""

# this program is created as of 15 Feb 2022

import datetime

MAX_YEAR = 2022
MIN_YEAR = 1920


def main():
    """Main"""
    dob_dict = create_dict()
    print_dict_age(dob_dict)


def create_dict():
    """Create dict from input"""
    dob_dict = {}
    for i in range(1, 5 + 1):
        name = input(f"Enter name {i}: ").title()
        while name in dob_dict:
            print(f"Name already exists in dictionary as {name} ({dob_dict[name]}).\nEnter another name..")
            name = input(f"Enter name {i}: ").title()
        while True:
            dob = input(f"Enter DOB {i} (dd/mm/yyyy): ")
            try:
                datetime.datetime.strptime(dob, '%d/%m/%Y')
                day, month, year = dob.split('/')
                year = int(year)
            except ValueError:
                print("The date of birth is not valid..")
            else:
                if MIN_YEAR > int(year) or int(year) > MAX_YEAR:
                    print("The date of birth is not valid..")
                else:
                    break
        dob_dict[name] = dob
    return dob_dict


def print_dict_age(dob_dict):
    """Print the ages from dict values"""
    # date taken for current age is on 31 Dec 2021.
    print("\nAges:")
    for name, dob in dob_dict.items():
        day, month, year = dob.split('/')
        year = int(year)
        if year > (MAX_YEAR - 1):
            age = "You will be born in the near future."
        else:
            age = (MAX_YEAR - 1) - year
        print(f"{name} ({age})")


main()
