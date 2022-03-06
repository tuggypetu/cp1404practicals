"""Guitar list from file with adding guitars to add to another csv file"""

from prac8.guitar import Guitar


def main():
    guitar_list = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        line = line.strip().split(',')
        guitar = Guitar(line[0], int(line[1]), float(line[2]))
        guitar_list.append(guitar)
    guitar_list.sort()
    for guitar in guitar_list:
        print(guitar)
    in_file.close()
    input_guitar(guitar_list)
    for guitar in guitar_list:
        print(guitar)
    out_file = open("myguitars.csv", "w")
    for guitar in guitar_list:
        guitar_line = [guitar.name, str(guitar.year), str(guitar.cost)]
        line = ','.join(guitar_line)
        out_file.write(f"{line}\n") if guitar != guitar_list[-1] else out_file.write(line)
    out_file.close()


def input_guitar(guitar_list):
    """Inputs for new guitar"""
    print()
    new_guitar = input("To add new guitar enter a: ").lower()
    while new_guitar == "a":
        name = input("Name: ").title()
        while name == "":
            print("Name cannot be empty.")
            name = input("Name: ").title()
        year = int((input("Year: ")))
        while len(str(year)) != 4 or year > 2022 or year < 1900:
            print("Invalid Year.")
            year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_list.append(Guitar(name, year, cost))
        print(guitar_list[-1])
        new_guitar = input("To add new guitar enter a: ").lower
    return guitar_list


main()
