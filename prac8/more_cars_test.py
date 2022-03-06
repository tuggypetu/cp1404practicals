"""Test classes in more cars"""

from prac8.more_cars import GasGussler, Bomb, EcoTaxi


def gas_gussler():
    """Test for gas_gussler class"""
    car = GasGussler("Tuggy", 100)
    car.drive(89)
    print(car)


def bomb():
    """Test for Bomb class"""
    car = Bomb("Tuggy", 100)
    car.drive(19)
    print(car)


def eco_taxi():
    """Test for eco taxi class"""
    car = EcoTaxi("Tuggy", 100)
    car.drive(19)
    print(car)
    print(car.get_fare())


# gas_gussler()
# bomb()
eco_taxi()
