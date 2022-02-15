"""Menu for name and addresses"""


def main():
    address_dict = {"Jordan": "Blk 18 Jalan Sultan 01-150", "Michael": "19 Hougang Avenue 3 01-185",
                    "Idiot": "141 MIDDLE ROAD, #06-05", "Retard": "501 ORCHARD ROAD, #04-09",
                    "Wangdu": "1 Sophia Road 03-23", "Kai": "5 Eng Kong Terrace"}
    print(f"Current dictionary is: {address_dict}")
    menu = "(E)nter a new name & address" \
           "\n(C)hange an address for an existing entry" \
           "\n(P)rint the address for a name you choose" \
           "\nChoose E, C, or P"
    print(menu)
    choice = input(">>> ").upper()
    while choice != "":
        if choice == "E":
            name = input("Enter name: ").title()
            address = input("Enter address: ").title()
            address_dict[name] = address
        elif choice == "C":
            name = input("Enter name: ").title()
            if name in address_dict:
                address = input(f"Enter new address for {name}: ").title()
                address_dict[name] = address
            else:
                print("Invalid. Name does not exist in dictionary.")
        elif choice == "P":
            name = input("Enter name: ").title()
            if name in address_dict:
                print(f"{name} lives in {address_dict[name]}.")
            else:
                print("Invalid. Name does not exist in dictionary.")
        else:
            print("Invalid choice")
        print(f"Current dictionary is: {address_dict}")
        print(menu)
        choice = input(">>> ").upper()
    print(f"\nThis is the dictionary at the end: {address_dict}")
    print("\nProgram has quit.")


main()
