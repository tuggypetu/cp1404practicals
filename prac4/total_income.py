"""Code for cumulative total income program"""


def main():
    """Display income report for incomes over a given number of months."""
    list_incomes = []
    month_num = int(input("How many months? "))
    while month_num < 0:
        print("Invalid month.")
        month_num = int(input("How many months? "))
    for i in range(1, month_num+1):
        income = float(input(f"Enter income for month {i}: "))
        list_incomes.append(income)
    print_report(list_incomes)


def print_report(list_incomes):
    """Prints income report"""
    print("\nIncome report\n-------------")
    # list_count = -1
    # for i in range(1, len(list_incomes) + 1):
    #     list_count += 1
    #     print(f"Month {i:2} - Income: $ {list_incomes[list_count]:10.2f}            "
    #           f"Total: $ {sum(list_incomes[0:list_count + 1]):10.2f}")
    total = 0
    for m, i in enumerate(list_incomes):
        total += i
        print(f"Month {m:2} - Income: ${i:10.2f}     Total: ${total:10.2f}")


main()
