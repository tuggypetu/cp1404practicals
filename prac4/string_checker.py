"""user enters unlimited strings and those repeated"""

string_list = []
repeat_list = []
string = input("Enter string: ").lower()
while string != '':
    if string in string_list:
        repeat_list.append(string)
    string_list.append(string)
    string = input("Enter string: ").lower()
if repeat_list:
    print(f"Strings repeated: {', '.join(repeat_list)}.")
else:
    print("No repeated strings entered")
