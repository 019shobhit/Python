# 1. Write a program to print multiplication table of a given number using for loop.


num = int(input("Enter number to print table of that number: "))

for i in range(1,11):
    print(num ,"X",i,"=",i*num)

