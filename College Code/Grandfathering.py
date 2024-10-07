# Python program for demonstrating multiple inheritance  
  
  
# Here, we will create the Base class 1  
class Mother1:  
    mothername1 = ""  
    def mother1(self):  
        print(self.mothername1)  
  
# Here, we will create the Base class 2  
class Father1:  
    fathername1 = ""  
    def father1(self):  
        print(self.fathername1)  
  
# now, we will create the Derived class  
class Son1(Mother1, Father1):  
    def parents1(self):  
        print ("Father name is :", self.fathername1)  
        print ("Mother name is :", self.mothername1)  
  
# Driver's code  
s1 = Son1()  
s1.fathername1 = "Rajesh"  
s1.mothername1 = "Shreya"  
s1.parents1()  