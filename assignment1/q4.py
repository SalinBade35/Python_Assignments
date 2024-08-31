# 4. WAP to enter a number from user and print reverse of it
# 153 --> 351

num1 = int(input("Entre number:  "))
num = num1
rev = 0
while num > 0:
    remainder = num % 10
    rev = (rev * 10) + remainder
    num = num // 10
print(f"{num1} --> {rev}")