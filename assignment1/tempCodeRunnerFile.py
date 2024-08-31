n = 3  # Number of rows

for i in range(n):
    # Print decreasing part of the pattern
    for j in range(i, 0, -1):
        print(j, end="")
    
    # Print the middle and increasing part of the pattern
    for j in range(i + 1):
        print(j, end="")
    
    print()  # Move to the next line after each row
