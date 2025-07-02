# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

dic = {}

n = input("Enter name: ")
l = input("Enter Fav Lang: ")
dic.update({n:l})
n = input("Enter name: ")
l = input("Enter Fav Lang: ")
dic.update({n:l})
n = input("Enter name: ")
l = input("Enter Fav Lang: ")
dic.update({n:l})

print(dic)