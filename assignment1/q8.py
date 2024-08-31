# 8. WAP to enter a number from user and print factorial of it
# 5! -- 5*4*3*2*1 --> 120

n = int(input("entre n: "))

factorial = 1

for i in range(1, n+1):
    factorial = factorial*i
        
print(factorial)