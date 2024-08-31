n = 4

for i in range(1, n + 1):
    for j in range(i, n):
        print(" ", end="")
    
    p = 1
    for j in range(2 * i - 1):
        print(p, end="")
        p += 1
    
    print()
