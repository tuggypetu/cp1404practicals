"""Car simulator"""

from prac6.car import Car

MENU = "Menu: \nd) drive \nr) refuel \nq) quit"


def main():
    """Main- Car Simulator"""
    print("Let's drive!")
    car_name = input("Enter your car name: ")
    while car_name == "":
        print("Invalid. Please enter car name")
        car_name = input("Enter your car name: ")
    car = Car(car_name, 100)
    print(car)
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "d":
            if car.fuel == 0:
                print("No fuel, cannot drive. Pls refill fuel.")
            else:
                drive_km = int(input("Enter number of km you want to drive: "))
                while drive_km < 0:
                    print("Distance must be >= 0")
                    drive_km = int(input("Enter number of km you want to drive: "))
                fuel_empty_string = " and ran out of fuel" if drive_km > car.fuel else ""
                distance = car.drive(drive_km)
                print(f"The car drove {distance}km{fuel_empty_string}.")
        elif choice == "r":
            fuel_u = int(input("Enter units of fuel do you want to add to the car: "))
            while fuel_u < 0:
                print("Fuel amount must be >= 0")
                fuel_u = int(input("Enter units of fuel do you want to add to the car: "))
            car.add_fuel(fuel_u)
            print(f"Added {fuel_u} units of fuel.")
        else:
            print("Invalid choice")
        print(f"\n{car}")
        print(MENU)
        choice = input("Enter your choice: ").lower()
    print(f"\nGood bye {car.name}'s driver.")


main()
