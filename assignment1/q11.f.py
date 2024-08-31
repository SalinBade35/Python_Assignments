n = 3  

for i in range(n):
    for j in range(i, n):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end="")
    
    
    for j in range(i + 1):
        print(j, end="")
    
    print()