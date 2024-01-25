# Number of rows
star_row = 5
# Create nested loops
for star in range(star_row + 1, 0, -1):
    for asterisk in range(0, star - 1):
        print("*", end=' ')
# Print
    print(" ")
