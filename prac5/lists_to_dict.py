"""Function that takes two parallel lists as input parameters and returns a dictionary"""


def main():
    """Lists and print dict - Main"""
    names = ["Jack", "Jill", "Harry"]
    dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
    dob_dict = list_to_dict(names, dates_of_birth)
    print(dob_dict)


def list_to_dict(key_list, value_list):
    """Convert 2 parallel lists to dict"""
    dob_dict = {}
    dob_str_list = []
    for (dd, mm, yyyy) in value_list:
        dob_str = f"{dd}/{mm}/{yyyy}"
        dob_str_list.append(dob_str)
    for i in range(len(key_list)):
        dob_dict[key_list[i]] = dob_str_list[i]
    return dob_dict


main()
