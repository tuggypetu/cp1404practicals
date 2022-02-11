
# Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
usr_name = input("Your name: ").title()
out_file = open("name.txt", 'w')
out_file.write(usr_name)
out_file.close()

# Write code that opens "name.txt" and reads the name (as above) then prints.
in_file = open("name.txt", 'r')
print(f"Your name is {in_file.readline()}")
in_file.close()

# Write code that opens "name.txt" and reads the name (as above) then prints. Version 2.
with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print("Your name is", name)

# Create a text file called numbers.txt and save it in your prac_02 directory.
# Put the following three numbers on separate lines in the file and save it:
# Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result.
in_file = open("numbers.txt", 'r')
nums = in_file.readlines()
add_value = int(nums[0]) + int(nums[1])
print(add_value)
in_file.close()

# Write fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.
in_file = open("numbers.txt", 'r')
total_added = 0
for i in in_file:
    num_text = int(i)
    total_added += num_text
print(total_added)
in_file.close()
