"""other recursions"""


def recurse_block(n):
    """number of rows from the user and calculate the number of blocks you will need to make a 2D pyramid"""
    if n > 0:
        return n + recurse_block(n-1)
    else:
        return 0

    # blocks = 0
    # listi = []
    # for i in range(1, rows+1):
    #     blocks += i
    #     listi.append(i)
    # print(blocks, 'blocks')
    # print(listi)


def distort_string(string, a=-1, z=0):
    """Print a string from the outside in"""
    a = a + 1
    z = z - 1
    is_even = True if len(string.strip()) % 2 == 0 else False
    num_to_return = (len(string.strip()) // 2) - 2 if is_even else -(len(string.strip()) // 2)
    if is_even:
        if num_to_return < a:
            return string[a] + ' ' + string[z]
    else:
        if num_to_return > z:
            return string[a]

    try:
        return_string = string[a] + ' ' + string[z] + ' ' + distort_string(string, a, z)
        return return_string
    except IndexError:
        return ''


def string_cleaner(string):
    """Cleans a string with only numbers and alphabets"""
    string_list = []
    for i in string:
        if i.isalnum():
            string_list.append(i)
    return ''.join(string_list)


def opp_string(string, z=0):
    """Return the opposite of the string (back to front)"""
    until_num = -(len(string.strip()))
    z -= 1
    if z >= until_num:
        return string[z] + opp_string(string, z)
    else:
        return ''


def palindrome(string):
    """Check if a string is a palindrome"""
    string = string_cleaner(string)
    if string.lower() == opp_string(string).lower():
        return True
    else:
        return False


if __name__ == '__main__':
    rows = int(input("Enter rows: "))
    # assert recurse_block(rows) == rows*(rows+1)/2
    print(rows*(rows+1)/2)
    print(recurse_block(rows), '\n')

    # assert distort_string("Programming") == "P g r n o i g m r m a"
    # assert distort_string("Progrmming") == "P g r n o i g m r m"
    print(distort_string("Programming"))
    print(distort_string("Progrmming"))
    string_to = input("Enter string: ")
    print(distort_string(string_to))
    print(palindrome("A Toyota's a Toyota"))
