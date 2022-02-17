"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac6.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My car", 180)
    my_car.drive(129)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    # New car called limo with 100u fuel
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Fuel in limo: {limo.fuel}")
    limo.drive(115)
    print(f"Limo odometer: {limo.odometer}")
    print(limo)


main()
