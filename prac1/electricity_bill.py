"""Electricity Bill Estimator"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator")
tariff_choice = input("Which tariff? 11 or 31: ")
while tariff_choice != "11" and tariff_choice != "31":
    print("Invalid tariff choice.")
    tariff_choice = input("Which tariff? 11 or 31: ")
if tariff_choice == "11":
    tariff = TARIFF_11
else:
    tariff = TARIFF_31
daily_kWh = float(input("Enter daily use in kWh: "))
num_days = int(input("Enter number of billing days: "))
est_bill = daily_kWh * tariff * num_days
print(f"Estimated bill: ${est_bill:.2f}")
