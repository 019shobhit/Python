# 1. Write a program using functions to find greatest of three numbers

def great(a,b,c):
    if(a>b and a>c):print(f"{a} is greatest")
    if(b>a and b>c):print(f"{b} is greatest")
    if(c>b and a<c):print(f"{c} is greatest")


great(3,6,5)