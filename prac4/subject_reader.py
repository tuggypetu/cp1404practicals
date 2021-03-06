"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Main function"""
    data = get_data()
    print(data)
    print("----------")
    inline_data(data)
    print("\n----------")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    full_list = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        full_list.append(parts)
        print(parts)  # See if that worked
        print("----------")
    input_file.close()
    return full_list


def inline_data(data):
    """Prints the data in proper sentences"""
    for i in data:
        print(f"{i[0]} is taught by {i[1]:12} and has {i[2]:3} students")


main()
