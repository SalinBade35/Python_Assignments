# 1
# 22
# 333
# 4444
# 55555

p=1
for i in range(5):
    for j in range(i+1):
        print(p, end="")
    p+=1
    print()
    