# 9. WAP to enter a limit from user and print fibonacii series
# 0 1 1 2 3 5 8 13 


n = int(input("Enter the limit: "))

# Initialize the first two numbers of the Fibonacci series
a, b = 0, 1

# Print the first two numbers
print(a, b, end=" ")

# Generate the Fibonacci series up to the limit
for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a, b = b, c

