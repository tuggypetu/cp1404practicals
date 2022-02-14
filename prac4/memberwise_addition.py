"""Take two lists, and return the list that contains the sum of elements in same index"""

# Lists for addition
LIST1 = [1, 2, 3]
LIST2 = [1, 2, 3, 4, 6, 7, 7, 8, 89]


def main():
    """Main function"""
    added_list = add_memberwise(LIST1, LIST2)
    print(added_list)


def add_memberwise(list1, list2):
    """Return added list"""
    added_list = []
    difference = abs(len(list1) - len(list2))
    if len(list1) > len(list2):
        for i in range(len(list2)):
            sum_index = list1[i] + list2[i]
            added_list.append(int(sum_index))
        for j in range(difference):
            sum_index = list1[len(list2) + j]
            added_list.append(int(sum_index))
    else:
        for i in range(len(list1)):
            sum_index = list1[i] + list2[i]
            added_list.append(int(sum_index))
        for j in range(difference):
            sum_index = list2[len(list1) + j]
            added_list.append(int(sum_index))
    return added_list


main()
