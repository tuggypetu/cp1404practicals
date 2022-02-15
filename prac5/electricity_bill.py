"""Electricity Bill Estimator 2.0"""

TARIFF_DICT = {"TARIFF_11": "0.244618", "TARIFF_31": "0.136928"}
for tariff in TARIFF_DICT:
    print(f"{tariff} = {TARIFF_DICT[tariff]}")

print("Electricity bill estimator 2.0")
tariff_choice = input("Which tariff? 11 or 31: ")
tariff_string = 'TARIFF_'+tariff_choice

while tariff_string not in TARIFF_DICT:
    print("Invalid tariff choice.")
    tariff_choice = input("Which tariff? 11 or 31: ")
    tariff_string = 'TARIFF_' + tariff_choice

tariff_float = float(TARIFF_DICT[tariff_string])
daily_kWh = float(input("Enter daily use in kWh: "))
num_days = int(input("Enter number of billing days: "))
est_bill = daily_kWh * tariff_float * num_days
print(f"Estimated bill: ${est_bill:.2f}")
