"""
CP1404/CP5632 Practical
Demo of sorting lists of 'compound' values
"""
from operator import itemgetter

names_with_ages = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]

# This sorts by the first value (name) in the element
names_with_ages.sort()
print(names_with_ages)

# This tells sort() to use the second (index 1, age) value in the element
names_with_ages.sort(key=itemgetter(1))
print(names_with_ages)

data = [['Derek', 7], ['Carrie', 7], ['Bob', 6], ['Aaron', 6]]
# This tells sort() to use the second (index 1) value...
# then the first (index 0) in the element
data.sort(key=itemgetter(1, 0))
print(data)

items = [('123', 'Derek', 'Smith', 7), ('124', 'Carrie', 'Brown', 7),
         ('125', 'Bob', 'Smith', 6), ('126', 'Aaron', 'Hewitt', 6)]
# The items will be sorted in the form: last name, first name
items.sort(key=itemgetter(2, 1))
print(items)

place_list = [['Lima', 'Peru', 3, 'n'], ['Oslo', 'Norway', 7, 'n'],
    ['Auckland', 'New Zealand', 1, 'v'], ['Rome', 'Italy', 12, 'n']]
place_list.sort(key=itemgetter(2))
place_list.sort(key=itemgetter(3))
print(place_list)

