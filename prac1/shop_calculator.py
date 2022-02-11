"""Calculate total price of shop items"""

total_price = 0
num_items = int(input("Number of items: "))
while num_items < 0:
    print("Invalid number of items!")
    num_items = int(input("Number of items: "))
for i in range(1, num_items + 1):
    price_item = float(input(f"Price of item {i}: "))
    total_price += price_item
if total_price > 100:
    total_price *= 0.9
print(f"Total price for {num_items} items is ${total_price:.2f}")
