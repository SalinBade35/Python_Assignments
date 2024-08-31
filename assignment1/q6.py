# 6. WAP to enter a number from user and check if it is pallindrome or not
# 121 - 121 
# 12321 - 12321

#palindrom : a word, phrase, or sequence that reads the same backwards as forwards

num1 = int(input("Entre number:  "))
num = num1
rev = 0
while num > 0:
    remainder = num % 10
    rev = (rev * 10) + remainder
    num = num // 10

if(rev == num1):
    print(f"{num1} is a palindrome number ")
    
else:
    print(f"{num1} is not a palindrome number")


