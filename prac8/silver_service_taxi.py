"""Silver Service Taxi"""

from prac8.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Taxi with more price per km"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}, has a {self.fanciness} in fanciness."

    def get_fare(self):
        """Override fare price for the Silver Taxi"""
        price_silver = self.flagfall + (super().get_fare())
        return price_silver
