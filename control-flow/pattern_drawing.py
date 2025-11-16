# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))
# Draw the Pattern
row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()
    row += 1