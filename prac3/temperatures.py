"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)


def main():
    """Main function- Get choices and while loop"""
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            t_celsius = float(input("Celsius: "))
            t_fahrenheit = c_to_f(t_celsius)
            print("Result: {:.2f} F".format(t_fahrenheit))
        elif choice == "F":
            t_fahrenheit = float(input("Fahrenheit: "))
            t_celsius = f_to_c(t_fahrenheit)
            print("Result: {:.2f} C".format(t_celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you. The end.")


def f_to_c(t_fahrenheit):
    """Convert F to C"""
    t_celsius = ((t_fahrenheit - 32) * 5) / 9
    return t_celsius


def c_to_f(t_celsius):
    """Convert C to F"""
    t_fahrenheit = t_celsius * 9.0 / 5 + 32
    return t_fahrenheit


main()
