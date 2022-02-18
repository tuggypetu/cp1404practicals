"""Test for guitar,py Guitar class"""

from prac6.guitar import Guitar

AGE_CALC = 2022
VINTAGE_AGE = 50

gibson_l5 = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_g = Guitar("Another Guitar", 2007, 9149.99)

guitar_dict_expected_age = {gibson_l5: 100, another_g: 15}
guitar_dict_expected_vintage = {gibson_l5: True, another_g: False}

for guitar in guitar_dict_expected_age:
    print(f"{guitar.name} get_age() - Expected {guitar_dict_expected_age[guitar]}. Got {guitar.get_age()}")
for guitar in guitar_dict_expected_vintage:
    print(f"{guitar.name} is_vintage() - Expected {guitar_dict_expected_vintage[guitar]}. Got {guitar.is_vintage()}")
