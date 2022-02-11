"""For Loops"""

for i in range(1, 20 + 1, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100

for i in range(0, 100 + 1, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1

for i in range(20, 1 - 1, -1):
    print(i, end=' ')
print()

# c. print n stars.
print()
num_stars = int(input("Number of stars: "))
for stars in range(num_stars):
    print("*", end='')
print()

# d. print n lines of increasing stars.
print()
num_stars = int(input("Number of stars: "))
for i in range(1, num_stars + 1):
    print("*" * i)
print()
