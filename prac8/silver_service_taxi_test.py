"""Silver Service Taxi test"""

from prac8.silver_service_taxi import SilverServiceTaxi

my_silver_car = SilverServiceTaxi('Silver Car', 100, 2)
print(my_silver_car.drive(18))
print(my_silver_car)
print(f"${my_silver_car.get_fare():.2f}")
