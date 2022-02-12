""""Quick Pick Lottery Ticket Generator"""

import random

NUM_LINES = 6
MIN = 1
MAX = 45


def main():
    """Main function to coordinate all functions"""
    q_picks = get_valid_input("How many quick picks? ")
    rand_table = gen_line(q_picks)
    gen_table(rand_table)


def get_valid_input(prompt):
    """Gets valid input for q_pick"""
    q_pick = int(input(prompt))
    while q_pick < 0:
        print("Invalid input")
        q_pick = int(input(prompt))
    return q_pick


def gen_line(q_picks):
    """Generates a line of random numbers and creates complete list"""
    rand_table = []
    rand_line = []
    for line in range(q_picks):
        for i in range(6):
            rand_num = random.randint(MIN, MAX+1)
            while rand_num in rand_line:
                rand_num = random.randint(MIN, MAX + 1)
            rand_line.append(rand_num)
            rand_line.sort()
        rand_table.append(rand_line)
        rand_line = []
    return rand_table


def gen_table(rand_table):
    """Prints the quick pick table"""
    for i in range(len(rand_table)):
        if i > 0:
            print()
        for num in range(NUM_LINES):
            print(rand_table[i][num], end=" ")


main()
