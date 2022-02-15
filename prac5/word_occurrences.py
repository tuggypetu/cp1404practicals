"""Count the occurrences of words in a string"""

string_dict = {}
get_string = input("Text: ").lower()
yolo_string = get_string.split()
for word in yolo_string:
    if word in string_dict:
        string_dict[word] += 1
    else:
        string_dict[word] = 1

    # also works from suggested solution >>
    # frequency = word_to_count.get(word, 0)
    # word_to_count[word] = frequency + 1

string_items = list(string_dict.keys())
print(string_items)
string_items.sort()
print(string_items)
width = max(len(words) for words in string_items)

for word in string_items:
    print(f"{word:{width+1}}: {string_dict[word]}")
