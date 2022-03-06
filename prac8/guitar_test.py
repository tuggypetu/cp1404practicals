"""write loop tuple for guitar csv"""

import csv
from collections import namedtuple


def main():
    Guitar = namedtuple('Guitar', 'name, year, cost')
    in_file = open("guitars.csv", "r")
    for guitar in map(Guitar._make, csv.reader(in_file)):
        print(guitar)


main()
