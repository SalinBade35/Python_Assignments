# 7. WAP to enter a number from user and print its individual digits on seperate line
# 153 
# 1 
# 5 
# 3 

num = int(input("Entre number:  "))

rev = 0
while num > 0:
    remainder = num % 10
    rev = (rev * 10) + remainder
    num = num // 10

num1 = rev

while num1 > 0:
    remainder = num1 % 10
    print(remainder)
    num1 = num1 // 10
