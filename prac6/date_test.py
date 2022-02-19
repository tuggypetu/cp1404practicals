"""Test Date class"""

import datetime
from prac6.date import Date

is_valid_date = False
date = input("Enter date (dd/mm/yyyy): ")
while not is_valid_date:
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
    except ValueError:
        print("The date of birth is not valid or in wrong format.. Correct is dd/mm/yyyy")
        date = input("Enter date (dd/mm/yyyy): ")

    else:
        is_valid_date = True

day, month, year = date.split('/')
day, month, year = int(day), int(month), int(year)

date = Date(day, month, year)
print(date, end='\n\n')

add_days = int(input("Enter number of days to add: "))
while add_days < 0:
    print("Invalid number of days to add. Must be greater than or equal to 0.")
    add_days = int(input("Enter number of days to add: "))
date.add_days(add_days)

print(date)
