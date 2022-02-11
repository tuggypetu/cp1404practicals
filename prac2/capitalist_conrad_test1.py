
import random

print("'' blank to wait for new day, 'q' to quit.")


def main():
    price = 10
    get_instruction = input("Enter instruction: ").upper()
    while get_instruction != 'Q':
        check_price(price)
        if get_instruction == '':
            rand_num = random.randint(1, 10)
            if rand_num < 6:
                rand_percent = random.uniform(0, 0.1)
                price *= (1 + rand_percent)
            else:
                rand_percent = random.uniform(0, 0.05)
                price *= (1 - rand_percent)
            print(f"The price is: ${price:.2f}")
            get_instruction = input("Enter instruction: ").upper()
        else:
            print("Invalid input.")
            get_instruction = input("Enter instruction: ").upper()
    print(f"You have quit the program. The price is ${price:.2f}")


def check_price(price):
    high_limit = 1000
    low_limit = 0.01
    if price > high_limit or price < low_limit:
        if price < 0:
            print("The program has quit. The price is $0.00")
        else:
            print(f"The program has quit. The price is ${price:.2f}")
        exit()
    else:
        pass


main()
