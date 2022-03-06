"""More cars"""

from prac8.car import Car
from prac8.taxi import Taxi


class GasGussler(Car):
    """Car uses more fuel than it should"""
    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        gas_distance = distance * 1.25
        if gas_distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= gas_distance
        self.odometer += distance
        return distance


class Bomb(Car):
    """Car does not move when driven, but still uses fuel"""
    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        return distance


class EcoTaxi(Taxi):
    """Car uses half the fuel and gives a percentage discount on the price per fare"""
    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        eco_distance = distance / 2
        if eco_distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= eco_distance
        self.odometer += distance
        self.current_fare_distance += distance
        return distance

    def get_fare(self):
        """Return the price for the taxi trip."""
        return round(self.price_per_km * self.current_fare_distance * 0.75, 1)
