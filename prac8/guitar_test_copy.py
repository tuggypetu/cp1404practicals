"""write loop tuple for guitar csv"""

import csv
from collections import namedtuple
from prac8.guitar import Guitar
from operator import itemgetter


def main():
    guitars_list = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        line = line.strip().split(',')
        print(line)
        guitar = Guitar(line[0], int(line[1]), float(line[2]))
        guitars_list.append(guitar)
    print()
    guitars_list.sort()
    print(guitars_list)
    print()
    for guitar in guitars_list:
        print(guitar)
    in_file.close()

    # Another version
    print("\nAnother version:")
    guitar_list = []
    Guitar_tuple = namedtuple('Guitar', ['name', 'year', 'cost'])
    in_file = open("guitars.csv", "r")
    reader = csv.reader(in_file)
    for row in reader:
        row[1], row[2] = int(row[1]), float(row[2])
        # print(row)
        guitar = Guitar_tuple._make(row)
        print(str(guitar))
        guitar_list.append(guitar)
    print()
    guitar_list.sort(key=itemgetter(1))
    print(repr(guitar_list))
    print()
    for guitar in guitar_list:
        print(guitar)
    in_file.close()

    print()
    yolo = input("Enter Yolo: ").lower()
    while yolo == "yolo":
        print("Invalid yolo.")
        yolo = input("Enter Yolo: ").lower()
    print("Yes that's the yolo")


main()
