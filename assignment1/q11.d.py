# 1
# 01
# 101
# 0101
# 10101
# 010101
# 1010101
# 01010101
# 101010101
# 0101010101

for i in range(10):
    for j in range(i+1):
        if((i+j)%2 == 0):
            print("1", end="")
        else:
            print("0",end="")
    print()
        
        

        