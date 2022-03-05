"""Taxi Simulator"""

from prac8.taxi import Taxi
from prac8.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Simulate Taxi choices and drive"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive")
    # Bills for each car is added because -
    # - the km on current fare was not displaying correctly when same car was driven twice.
    bill, bill_1, bill_2, bill_3 = 0, 0, 0, 0
    choice_taxi = None
    choice = input(f"{MENU}\n>>> ").lower()
    while choice != "q":
        if choice == "c":
            display_taxis(taxis, "Taxis available: ")
            choice_taxi = get_valid_taxi("Enter taxi choice number: ")
        elif choice == "d":
            if choice_taxi is not None:
                bill_ride = get_valid_distance("Drive how far? ", taxis, choice_taxi, bill_1, bill_2, bill_3)
                bill_1 += bill_ride if choice_taxi == 1 else 0
                bill_2 += bill_ride if choice_taxi == 2 else 0
                bill_3 += bill_ride if choice_taxi == 3 else 0
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid Choice")
        bill = bill_1 + bill_2 + bill_3
        print(f"Bill to date: ${bill:.2f}")
        choice = input(f"{MENU}\n>>> ").lower()
    print(f"Total trip cost: ${bill:.2f}")
    display_taxis(taxis, "Taxis are now: ")


def display_taxis(taxis, prompt):
    """Display Taxis in the list"""
    print(prompt)
    for i, taxi in enumerate(taxis, 1):
        print(i, "-", taxi)


def get_valid_taxi(prompt):
    """Get a valid taxi from list"""
    try:
        choice_taxi = int(input(prompt))
    except ValueError:
        print("Taxi choice must a number")
    else:
        if choice_taxi in [1, 2, 3]:
            return choice_taxi
        else:
            print("Invalid taxi choice")


def get_valid_distance(prompt, taxis, choice_taxi, bill_1, bill_2, bill_3):
    """Get valid distance for driving"""
    try:
        drive_to = float(input(prompt))
    except ValueError:
        print("Distance must be a number")
        return 0
    else:
        if drive_to < 0:
            print("Distance must be a greater than 0")
            return 0
        else:
            taxis[choice_taxi - 1].drive(drive_to)
            fare_ride = taxis[choice_taxi - 1].get_fare()
            if choice_taxi == 1:
                fare_ride -= bill_1 if bill_1 != 0 else 0
            elif choice_taxi == 2:
                fare_ride -= bill_2 if bill_2 != 0 else 0
            else:
                fare_ride -= bill_3 if bill_3 != 0 else 0
            print(f"Your {taxis[choice_taxi - 1].name} trip cost you ${fare_ride:.2f}")
            return fare_ride


def drive_taxi(taxis, choice_taxi, drive_to):
    """Drive the chosen taxi"""
    taxis[choice_taxi - 1].drive(drive_to)
    print(f"Your {taxis[choice_taxi - 1].name} trip cost you ${taxis[choice_taxi - 1].get_fare():.2f}")
    return taxis[choice_taxi - 1].get_fare()


if __name__ == '__main__':
    main()
