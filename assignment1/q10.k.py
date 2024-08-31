# 1
# 23
# 456
# 78910
p=1
for i in range(4):
    for j in range(i+1):
        print(p, end="")
        p+=1
    print()