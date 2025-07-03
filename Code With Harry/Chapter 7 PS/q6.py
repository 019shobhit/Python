# 6. Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter number: "))

f =1
for i in range (1,n+1):
    f*=i
    print(f)