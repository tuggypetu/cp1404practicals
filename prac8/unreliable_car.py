"""
Unreliable car -
it has another variable reliability: a float between 0 and 100,
that represents the percentage chance that the drive method will actually drive the car
"""

from prac8.car import Car
import random


class UnreliableCar(Car):
    """Specialised car that has reliability variable"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    # def __str__(self):

    def drive(self, distance):
        """Drive like parent Car but with reliability attribute"""
        rand_num = random.randint(0, 100)
        if rand_num >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
