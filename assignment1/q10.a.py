#wap to print following patterns:

# *
# **
# ***
# ****
# *****

for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()