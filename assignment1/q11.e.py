#    1
#   121
#  12321
# 1234321

for i in range(1, 5):
    
    for j in range(i, 5):
        print(" ", end="")

    p = 1
    for j in range(i):
        print(p, end="")
        p += 1

    p -= 2
    for j in range(i - 1):
        print(p, end="")
        p -= 1

    print()  # Move to the next line after each row
