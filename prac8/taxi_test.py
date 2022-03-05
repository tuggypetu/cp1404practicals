"""Test the taxi class"""

from prac8.taxi import Taxi

prius1_taxi = Taxi('Prius 1', 100)
prius1_taxi.drive(40)
print(prius1_taxi)
prius1_taxi.start_fare()
prius1_taxi.drive(100)
print(prius1_taxi)
