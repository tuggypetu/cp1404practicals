"""Guitar list n print"""

from prac6.guitar import Guitar


def main():
    """Main- My guitars"""
    guitar_list = []
    print("My guitars!")
    input_guitar(guitar_list)


def input_guitar(guitar_list):
    """Inputs for new guitar"""

    guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    name = input("Name: ").title()
    while name != "":
        year = int((input("Year: ")))
        while len(str(year)) != 4 or year > 2022 or year < 1900:
            print("Invalid Year.")
            year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_list.append(Guitar(name, year, cost))
        print(guitar_list[-1])
        name = input("Name: ").title()

    guitar_print(guitar_list)
    return guitar_list


def guitar_print(guitar_list):
    """Print guitar list"""

    name_width = max(len(guitar.name) for guitar in guitar_list)
    cost_width = max(len(f"{guitar.cost:,.2f}") for guitar in guitar_list)

    guitar_list.sort()
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitar_list, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ''
        print(f"Guitar {i}: {guitar.name:>{name_width+2}} ({guitar.year}), worth ${guitar.cost:>{cost_width+1},.2f} "
              f"{vintage_string}")


main()
