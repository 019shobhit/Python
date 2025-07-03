# 4. Write a program to find whether a given number is prime or not.

n = int(input("Enter number : "))

# for i in range (2,n):
#     if(n%i==0):
#         print("Enven number")
#         break
# else: print("Odd number")

i =2
while(i*i<=n):
    if(n%i==0):
        print("Enven number")
        break
    i+=1

else:print("Odd")