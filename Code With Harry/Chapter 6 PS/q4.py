# 4. Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter Username: ")

if(len(username) <10):
    print(username,"havinf less than 10 characters")
else:print(username,"having equal to or more than 10 character")
