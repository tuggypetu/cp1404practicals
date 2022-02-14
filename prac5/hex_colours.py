"""Hexadecimal colour code dict"""

HEXA_COLOUR = {"amethyst": "#9966cc", "bittersweet shimmer": "#bf4f51", "cadetblue2": "#8ee5ee", "thistle": "#d8bfd8",
               "zaffre": "#0014a8", "viridian": "#40826d", "springgreen3": "#00cd66", "ruby": "#e0115f",
               "nyanza": "#e9ffdb", "jonquil": "#f4ca16"}

print("GET HEXADECIMAL COLOUR CODE")
ent_colour = input("Enter colour name: ").lower()
while ent_colour != '':
    if ent_colour in HEXA_COLOUR:
        print("Code: ", HEXA_COLOUR[ent_colour])
    else:
        print("Invalid colour")
    ent_colour = input("Enter colour name: ").lower()
print("\nThe program has ended.")
