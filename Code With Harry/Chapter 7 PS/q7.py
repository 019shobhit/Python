# pattern printing

#   *
#  ***
# *****

# n = int(input("Enter number: "))
n=5

for i in range(0,n):
    print(" "*(n-i-1),end="")
    print("*"*(i*2+1),end="")
    print()