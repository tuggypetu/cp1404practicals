"""
Email and name dict
"""

email_dict = {}
get_email = input("Email: ")
while get_email != '':
    e_name = get_email.split('@')[0]
    name_from_email = e_name.split('.')
    yolo_name = ' '.join(name_from_email).title()
    is_it_name = input(f"Is your name {yolo_name}? (Y/n) ").upper()
    if is_it_name != "Y" and is_it_name != "":
        get_name = input("Name: ").title()
        email_dict[get_email] = get_name
    else:
        email_dict[get_email] = yolo_name
    get_email = input("Email: ")
print()
for eml, name in email_dict.items():
    print(f"{name} ({eml})")
