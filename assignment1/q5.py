#5. WAP to enter a number from user and print sum of its individual digits
# 153 --> 9

n = int(input("n:  "))
sum = 0
while(n > 0):
    remainder = n % 10
    n = n // 10
    sum = sum + remainder
print(sum) 