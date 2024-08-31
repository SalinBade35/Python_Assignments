# 1. WAP to enter a character from user and check if it is vowel or consonant

value = input("entre an alphabet: ")
value = value.lower()
if(value == "a" or value == "e" or value == "i" or value == "o" or value == "u"):
    print(f"{value} is vowel letter")
else:
    print(f"{value} is consonant letter")
    
    