"""
Travel Tracker 1.0

Name: Siddhanth Biswas
Date started: 20/02/2022
GitHub URL:
"""

from operator import itemgetter
import random

MENU = "\nMenu:\nL - List places\nR - Recommend random place\nA - Add new place\nM - Mark a place as visited\nQ - Quit"
FILE_NAME = "places.csv"


def main():
    """Travel Tracker 1.0"""
    print("Travel Tracker 1.0 - by Siddhanth Biswas")
    place_list = read_file()
    print(f"{len(place_list)} places loaded from {FILE_NAME}")
    print(MENU)
    c = input(">>> ").upper()
    while c != "Q":
        if c == "L":
            list_places(place_list)
        elif c == "R":
            random_place(place_list)
        elif c == "A":
            place_list = add_place(place_list)
        elif c == "M":
            place_list = mark_visited(place_list)
        else:
            print("Invalid menu choice")
        print(MENU)
        c = input(">>> ").upper()
    file = open(FILE_NAME, 'w')
    print(f"{len(place_list)} places saved to {FILE_NAME}\nHave a nice day :)"
          f"\n\nAt the end of this run, the saved CSV file contained:")
    for place in place_list:
        place[2] = str(place[2])
        data = ','.join(place)
        print(data)
        file.write(f"{data}\n") if place != place_list[-1] else file.write(f"{data}")
    file.close()


def read_file():
    """Read data from file"""
    file = open(FILE_NAME, 'r')
    place_list = []
    for line in file:
        line = line.strip()
        line = line.split(',')
        line[2] = int(line[2])
        place_list.append(line)
    file.close()
    place_list.sort(key=itemgetter(-1, 2))
    return place_list


def list_places(place_list):
    """List places"""
    city_width = max(len(place[0]) for place in place_list)
    country_width = max(len(place[1]) for place in place_list)
    visit_counter = 0
    for i, place in enumerate(place_list, 1):
        visit_counter = visit_counter + 1 if place[-1] == 'n' else visit_counter
        visit_string = '*' if place[-1] == 'n' else ' '
        print(f"{visit_string}{i:>2}. {place[0]:>{city_width}} in {place[1]:>{country_width}} {place[2]:>2}")
    print(f"{len(place_list)} places. You still want to visit {visit_counter} places.")
    return visit_counter


def random_place(place_list):
    """Recommend random place"""
    visit_counter = 0
    for place in place_list:
        visit_counter = visit_counter + 1 if place[-1] == 'n' else visit_counter
    if visit_counter == 0:
        print("No more new places to visit.")
    else:
        ran_place = random.randint(0, visit_counter - 1)
        print(f"Not sure where to visit next?\nHow about... {place_list[ran_place][0]} in {place_list[ran_place][1]}?")


def add_place(place_list):
    """Add new place"""
    city = input("City name: ").title()
    while city == "":
        print("Input cannot be empty")
        city = input("City name: ")
    country = input("Country: ").title()
    while country == "":
        print("Input cannot be empty")
        country = input("Country: ")
    is_int = False
    while not is_int:
        priority = input("Priority: ")
        try:
            int(priority)
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            priority = int(priority)
            if priority < 1:
                print("Priority must be > 0")
            else:
                new_place = [city, country, priority, 'n']
                place_list.append(new_place)
                print(f"{city} in {country} (priority {priority}) added to Travel Tracker")
                is_int = True
    place_list.sort(key=itemgetter(-1, 2))
    return place_list


def mark_visited(place_list):
    """Mark an unvisited place as visited"""
    visit_counter = list_places(place_list)
    in_list = False
    while not in_list:
        place_mark = input("Enter the number of a place to mark as visited\n>>> ")
        try:
            int(place_mark)
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            place_mark = int(place_mark)
            if place_mark < 1:
                print("Number must be > 0")
            elif place_mark > len(place_list):
                print("Invalid place number")
            elif place_mark > visit_counter:
                print(f"{place_list[place_mark-1][0]} in {place_list[place_mark - 1][1]} is already visited earlier.")
                in_list = True
            else:
                place_list[place_mark - 1][-1] = 'v'
                print(f"{place_list[place_mark-1][0]} in {place_list[place_mark-1][1]} visited!") \
                    if place_list[place_mark-1][-1] == 'v' else print("error")
                in_list = True
    place_list.sort(key=itemgetter(-1, 2))
    return place_list


if __name__ == '__main__':
    main()
