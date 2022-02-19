"""Person List and print"""

from prac6.person import Person


def main():
    """Main"""
    print("Add people to get table printed.")
    person_list = person_info()
    table_print(person_list)


def person_info():
    """Choices in menu"""
    person_list = []
    f_name = input("Enter first name: ").title()
    while f_name != '':
        l_name = input("Enter last name: ").title()
        age = int(input("Enter age: "))
        while age < 0 or age > 120:
            print("Invalid age")
            age = int(input("Enter age: "))
        person_list.append(Person(f_name, l_name, age))
        print(person_list[-1])
        f_name = input("Enter first name: ").title()
    person_list.append(Person("John", "Smith", 51))
    person_list.append(Person("Pat", "Cummins", 28))
    return person_list


def table_print(person_list):
    """Prints table of list"""
    f_width = max(len(person.first_name) for person in person_list)
    l_width = max(len(person.last_name) for person in person_list)
    person_list.sort()
    print("\nPeople:")
    for i, retard in enumerate(person_list, 1):
        print(f"Person {i:2} : {retard.first_name:>{f_width+1}} {retard.last_name:>{l_width+1}} {retard.age:3}")


main()
