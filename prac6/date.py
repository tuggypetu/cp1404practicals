"""Date class"""


class Date:
    def __init__(self, date=0, month=0, year=0):
        """Initialise"""
        self.date = date
        self.month = month
        self.year = year

    def __str__(self):
        """Return string"""
        return f"Date: {self.date}/{self.month}/{self.year}"

    def add_days(self, n):
        """Add n days to date"""

        n = int(n)
        month_135781012 = 31
        month_46911 = 30
        month_2 = 29 if self.year % 4 == 0 else 28
        month_day_tuple = (month_135781012, month_2, month_135781012, month_46911, month_135781012, month_46911,
                           month_135781012, month_135781012, month_46911, month_135781012, month_46911, month_135781012)
        while n != 0:
            for i, num_days in enumerate(month_day_tuple, 1):
                if self.date == 31 and self.month == 12:
                    self.year += 1
                    self.month = 1
                    self.date = 1
                    n -= 1
                else:
                    if i == self.month:
                        if self.date != num_days:
                            if (self.date + n) > num_days:
                                n = n - (num_days - self.date)
                                self.date = num_days
                            else:
                                self.date = self.date + n
                                n = 0
                        else:
                            self.month += 1
                            self.date = 1
                            n -= 1
