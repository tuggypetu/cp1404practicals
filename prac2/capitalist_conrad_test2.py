
import random


def main():
    price = 10
    print(f"Starting price: ${price:,.2f}")
    day = 0
    while True:
        check_price(price, day)
        day += 1
        rand_num = random.randint(1, 10)
        if rand_num < 6:
            rand_percent = random.uniform(0, 0.1)
            price *= (1 + rand_percent)
        else:
            rand_percent = random.uniform(0, 0.05)
            price *= (1 - rand_percent)
        print(f"The day {day} price is: ${price:,.2f}")


def check_price(price, day):
    high_limit = 1000
    low_limit = 0.01
    if price > high_limit or price < low_limit:
        print()
        if price < 0:
            print("The program has quit. The price is $0.00")
        else:
            print(f"The program has quit.\nThe price is ${price:,.2f} after {day} days.")
        exit()
    else:
        pass


main()
